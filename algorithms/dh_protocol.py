"""
based on
"""

from random import randint

N_DIGITS_A, N_DIGITS_B = 5, 5
PG_MIN, PG_MAX = 100, 1000


def test_dh(n_test: int = 100):
    for _ in range(n_test):
        deffie_hellman_protocol()


def deffie_hellman_protocol():
    a = get_rand_int(N_DIGITS_A)
    b = get_rand_int(N_DIGITS_B)

    p, g = randint(10, PG_MAX), randint(1, PG_MIN)

    A = (g ** a) % p
    B = (g ** b) % p

    key_a = (B ** a) % p  # equal with g^ab mode p
    key_b = (A ** b) % p  # equal with g^ab mode p

    assert key_a == key_b


def get_rand_int(n_digits: int) -> int:
    return randint(10 ** (n_digits - 1), 10 ** n_digits)


if __name__ == '__main__':
    test_dh()
