import contextlib
import random

from tempfile import NamedTemporaryFile
from threading import Thread
from queue import Queue
from typing import Optional
from subprocess import Popen, PIPE, STDOUT

import requests
from requests.exceptions import ConnectionError

import os
from os import environ as env

from birdwell.utils.time import stale, rn
from datetime import timedelta


class VPNController:
    ip_server = 'https://api.brd.cx/utils/ip'

    @classmethod
    def get_ip(cls, retries=1):
        try:
            resp = requests.get(cls.ip_server).json()
        except ConnectionError as e:
            if retries > 0:
                return cls.get_ip(retries - 1)
            else:
                raise e

        return resp.get('ip')

    @classmethod
    def from_env(cls, verbosity=0):

        routes = [
            tuple(x.replace('(', '')
                  .replace(')', '')
                  .replace(' ', '')
                  .split(','))
            for x in env.get('VPN_EXCLUDED_ROUTES', '').split('),(')]

        return cls(
            username=env.get('VPN_USER'),
            password=env.get('VPN_PASS'),
            server=env.get('VPN_SERVER'),
            protocol=env.get('VPN_PROTOCOL'),
            excluded_routes=routes,
            verbosity=verbosity
        )

    def __init__(self,
                 username: str,
                 password: str,
                 server: Optional[str] = None,
                 protocol: Optional[str] = 'udp',
                 excluded_routes: Optional[list[tuple[str, ...]]] = None,
                 verbosity=0,
                 server_filter: Optional[str] = None,
                 cached_ip_duration: timedelta | None = timedelta(seconds=5)
                 ):
        self.verbosity = verbosity

        self._server_list = None
        self.protocol = protocol if protocol else 'udp'
        self._server = server
        self._server_filter = server_filter if server_filter else ''
        self.excluded_routes = excluded_routes

        self.username = username
        self.password = password

        self.process: Popen | None = None
        self._reader: Thread | None = None

        self.running = False
        self.initialized = False

        self.oq = None

        self.origin_ip = self.get_ip()
        self.ip_cache_time = cached_ip_duration
        self._ip = None

    @property
    def ip(self):
        if (not self.ip_cache_time  # caching disabled
                or not self.ip  # ip not initialized
                or stale(self._ip['ts'], self.ip_cache_time)):  # stale ip

            self._ip = {'ip': self.get_ip(), 'ts': rn()}

        return self._ip['ip']

    def _v1print(self, *stuff):
        if self.verbosity >= 1:
            print(*stuff)

    def _v2print(self, *stuff):
        if self.verbosity >= 2:
            print(*stuff)

    def _v3print(self, *stuff):
        if self.verbosity >= 3:
            print(*stuff)

    @property
    def server(self):
        if self._server:
            return self._server
        return random.choice(self.server_list)

    @property
    def reader(self):
        if self._reader and not self._reader.is_alive():
            self._reader = None
        return self._reader

    def new_reader(self):
        while self.reader:
            self.running = False

        self.running = True
        self.oq = Queue()
        self._reader = Thread(target=self.read_cxn, daemon=True)
        self._reader.start()

    @contextlib.contextmanager
    def connection(self, server: Optional[str] = None, protocol: Optional[str] = 'udp'):
        if self.process:
            raise NotImplementedError("VPN already active. Double VPN not allowed.")
        self._v2print(f'PRE-VPN IP: {self.get_ip()}')
        vpn_server = server if server else self.server
        vpn_protocol = protocol if protocol else self.protocol

        with self.start_command(vpn_server, vpn_protocol) as cxn_cmd:
            self._v2print(f'Connecting to {self.server} with protocol {self.protocol} with CMD: {cxn_cmd}.')

            self.initialized = False

            self.process = Popen(cxn_cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
            self.new_reader()

            # stop and remove old reader, reset queue, init new thread and start thread

            self._v2print('Initializing VPN Connection...')
            while not self.initialized:
                # print('attempting to read line...')
                line = self.oq.get()
                if 'Initialization Sequence Completed' in line:
                    self._v2print('Connection Initialized Successfully!')
                    self.initialized = True
                elif 'Exiting due to fatal error' in line:
                    self.running = False
                    raise Exception('Fatal Error During VPN Initialization!')

        self._v1print(f'VPN ENABLED. IP NOW: {self.get_ip()}')

        try:
            if self.process and self.process.poll() is None:
                yield True
            else:
                raise ConnectionError('VPN OFFLINE')

        finally:
            self.active = False
            self._v1print(f'VPN DISABLED. IP REVERTED TO: {self.get_ip()}')

    @contextlib.contextmanager
    def start_command(self, server, protocol):
        tf = NamedTemporaryFile(mode='w')
        tf.write(self.username + '\n')
        tf.write(self.password + '\n')
        tf.flush()

        config_file = f'/etc/openvpn/ovpn_{protocol}/{server}.nordvpn.com.{protocol}.ovpn'

        cxn_cmd = [
            "openvpn",
            "--config", config_file,  # which server to connect to
            '--auth-user-pass', tf.name,  # username and pass pulled from tempfile
        ]

        if self.excluded_routes:
            for x in self.excluded_routes:
                cxn_cmd += ['--route', x[0], x[1], 'net_gateway']

        try:
            yield cxn_cmd

        finally:
            self._v2print('Closing Temp File')
            tf.close()

    @property
    def server_filter(self):
        return self._server_filter

    @server_filter.setter
    def server_filter(self, val):
        if val is None:
            val = ''
        self._server_filter = val
        self._server_list = None

    @property
    def server_list(self):
        if not self._server_list:
            self._server_list = [
                server for x in os.listdir(f'/etc/openvpn/ovpn_{self.protocol}')
                if (server := x.split('.')[0]).startswith(self.server_filter)
            ]
        return self._server_list

    @property
    def active(self) -> bool:
        return not self.process.poll() and self.initialized

    @active.setter
    def active(self, val):
        if val is not False:
            raise ValueError('Can only use to deactivate current VPN.')

        self._v2print('Deactivating VPN.')
        if proc := self.process:
            self._v2print('Terminating Process.')
            proc.terminate()
            self._v2print('Waiting for process termination.')
            proc.wait()
            self._v2print(f'Completed with exit code: {proc.returncode}.')

        self._v2print('Cleaning up.')
        self.process = None
        self.running = False
        self.initialized = False
        self._v2print('Deactivation Complete.')

    def read_cxn(self):
        while self.running:
            msg = self.process.stdout.readline()
            if not msg:
                continue
            line = msg.decode()
            self._v3print(line)
            self.oq.put(line)
        self._v2print('Reader Thread Exiting.')
