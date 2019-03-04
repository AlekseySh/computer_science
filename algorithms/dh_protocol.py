"""
based on
https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
"""

from random import randint

N_DIGITS_A, N_DIGITS_B = 5, 5
PG_MIN, PG_MAX = 100, 1000


def test_dh(n_test=100):
    for _ in range(n_test):
        deffie_hellman_protocol()


def deffie_hellman_protocol():
    # all variables without prefix 'secret' are public
    secret_a = get_rand_int(N_DIGITS_A)
    secret_b = get_rand_int(N_DIGITS_B)

    p, g = randint(10, PG_MAX), randint(1, PG_MIN)

    a = (g ** secret_a) % p
    b = (g ** secret_b) % p

    secret_val_a = (b ** secret_a) % p  # equal with g^ab mode p
    secret_val_b = (a ** secret_b) % p  # equal with g^ab mode p

    assert secret_val_a == secret_val_b


def get_rand_int(n_digits):
    return randint(10 ** (n_digits - 1), 10 ** n_digits)


if __name__ == '__main__':
    test_dh()
