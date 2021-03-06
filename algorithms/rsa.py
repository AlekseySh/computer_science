"""
based on
https://en.wikipedia.org/wiki/RSA_(cryptosystem)
"""

from random import choice, randint

import pyprimes as prime
from tqdm import tqdm

from algorithms.gcd import euclidian as gcd
from algorithms.gcd import euclidian_ext as egcd

# params
PQ_MIN = 10e2
EXP_MAX = 10e2
MSG_MIN = 10e1
MSG_MAX = 10e2


def test_rsa(n_test=100):
    print('Start testing RSA protocol.')

    for _ in tqdm(range(n_test)):
        rsa_session()

    print(f'All {n_test} rsa-tests passed!')


def rsa_session(msg_min=MSG_MIN,
                msg_max=MSG_MAX
                ):
    message = randint(msg_min, msg_max)
    (n, e), (n, d) = generate_keys()

    msg_crypted = (message ** e) % n  # using only public key
    msg_decrypted = (msg_crypted ** d) % n  # using private

    assert msg_decrypted == message, \
        f'message: {message}, ' \
        f'crypted message {msg_crypted},' \
        f'decrypted message: {msg_decrypted},' \
        f'public exp: {e},' \
        f'secret d: {d},' \
        f'module n: {n}.'


def generate_keys():
    p, q = generate_pq()
    n = p * q
    lam = lcm(p - 1, q - 1)
    e = generate_pub_exp(lam)  # public value
    d = modular_inv(e, lam)  # hold in secrete
    public = (n, e)
    private = (n, d)
    return public, private


def generate_pq(min_val=PQ_MIN):
    p_times, q_times, max_times = None, None, 10
    p, q = None, None

    while p_times == q_times:
        p_times = randint(1, max_times)
        q_times = randint(1, max_times)

    prime_gen = prime.primes_above(min_val)

    for _ in range(p_times):
        p = next(prime_gen)

    for _ in range(q_times):
        q = next(prime_gen)

    return p, q


def generate_pub_exp(lam, max_val=EXP_MAX):
    primes = list(prime.primes_below(min(max_val, lam)))

    e = choice(primes)
    while (lam % e == 0) or (e < 10):
        e = choice(primes)

    return e


def lcm(a, b):
    return abs(a * b) / gcd(a=a, b=b)


def modular_inv(a, b):
    g, x, _ = egcd(a, b)
    if g == 1:
        return int(x % b)
    else:
        raise ValueError(f'Modular inv for ({a}, {b}) does not exist')


if __name__ == '__main__':
    test_rsa()
