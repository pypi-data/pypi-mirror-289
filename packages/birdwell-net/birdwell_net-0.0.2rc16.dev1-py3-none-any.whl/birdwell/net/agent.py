import random


def user_agent() -> dict:
    return {
        'User-Agent': random.choice([
            f'(Windows NT 1{random.randint(0, 1)}.0; Win64; x64)',
            f'(Macintosh; Intel Mac OS X {random.randint(800, 1015) / 100}; rv:{random.randint(80, 120)}.0)',
            f'(X11; {random.choice(['', 'Fedora; ', 'Ubuntu; '])}Linux x86_64; rv:{random.randint(80, 120)}.0)',
        ])}
