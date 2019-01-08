from random import randint

__all__ = [
    'euclidian', 'euclidian_recursive',
    'euclidian_ext_recursive', 'euclidian_ext'
]


# FIND GCD

def euclidian(a: int, b: int) -> int:
    a, b = normolize_input(a, b)

    if b == 0:
        return a

    r = a % b
    while r != 0:
        b, r = r, b % r
    return b


def euclidian_recursive(a: int, b: int) -> int:
    a, b = normolize_input(a, b)

    if b == 0:
        return a

    return euclidian_recursive(b, a % b)


def normolize_input(a, b):
    a, b = abs(a), abs(b)
    a, b = max(a, b), min(a, b)
    return a, b


def check_is_gcd(a, b, gcd: int):
    def check_is_cd(d):
        return (a % d == 0) and (b % d == 0)

    if not check_is_cd(gcd):
        return False

    for i in range(gcd + 1, min(a, b) + 1):
        if check_is_cd(i):
            return False

    return True


def test_gcd(gcd_finder,
             n_test=100,
             bounds=(-100, 100)
             ):
    for _ in range(n_test):
        a, b = randint(*bounds), randint(*bounds)
        gcd = gcd_finder(a, b)
        assert check_is_gcd(a, b, gcd), \
            f'{gcd} is not GCD for {a} and {b}'


# FIND BEZOUT COEFFICIENTS
# x * a + y * b = gcd(a, b)

def euclidian_ext(a: int, b: int) -> (int, int, int):
    x, y = 0, 1
    x1, y1 = 1, 0

    while a != 0:
        q = b // a
        b, a = a, b % a
        y, y1 = y1, y - q * y1
        x, x1 = x1, x - q * x1
    return b, x, y


def euclidian_ext_recursive(a: int, b: int) -> (int, int, int):
    if a == 0:
        gcd, x, y = b, 0, 1
        return gcd, x, y

    gcd, x, y = euclidian_ext_recursive(b % a, a)
    x_new = y - (b // a) * x
    y_new = x
    return gcd, x_new, y_new


def test_gcd_decomposition(gcd_decompositor,
                           n_test=100,
                           bounds=(-100, 100)
                           ):
    for _ in range(n_test):
        a, b = randint(*bounds), randint(*bounds)
        gcd, x, y = gcd_decompositor(a, b)
        assert x * a + y * b == gcd, \
            f'{x}*{a} + {y}*{b} != {gcd}'


def main():
    test_gcd(gcd_finder=euclidian)
    test_gcd(gcd_finder=euclidian_recursive)
    test_gcd_decomposition(gcd_decompositor=euclidian_ext)
    test_gcd_decomposition(gcd_decompositor=euclidian_ext_recursive)


if __name__ == '__main__':
    main()
