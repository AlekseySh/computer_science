from random import randint

__all__ = ['euclidian', 'euclidian_recursive']


def euclidian(a: int, b: int) -> int:
    a, b = normolize_input(a, b)

    if (a == 0) or (b == 0):
        return max(a, b)

    r = a % b
    while r != 0:
        b, r = r, b % r
    return b


def euclidian_recursive(a: int, b: int) -> int:
    a, b = normolize_input(a, b)

    if (a == 0) or (b == 0):
        return max(a, b)

    return euclidian_recursive(b, a % b)


def normolize_input(a, b):
    a, b = abs(a), abs(b)
    a, b = max(a, b), min(a, b)
    return a, b


def check_is_gcd(a: int, b: int, gcd: int) -> bool:
    def check_is_cd(d):
        return (a % d == 0) and (b % d == 0)

    if not check_is_cd(gcd):
        return False

    for i in range(gcd + 1, min(a, b) + 1):
        if check_is_cd(i):
            return False

    return True


def test(gcd_finder, n_test=100, bounds=(-100, 100)):
    for _ in range(n_test):
        a, b = randint(*bounds), randint(*bounds)
        gcd = gcd_finder(a, b)
        assert check_is_gcd(a, b, gcd)


def main():
    test(gcd_finder=euclidian_recursive)
    test(gcd_finder=euclidian)


if __name__ == '__main__':
    main()
