from random import randint


def euclidian(a: int, b: int) -> int:
    if (a == 0) or (b == 0):
        return max(abs(a), abs(b))

    return 1


def recursive(a: int, b: int) -> int:
    if (a == 0) or (b == 0):
        return max(abs(a), abs(b))
    return recursive(b, a % b)


def check_is_gcd(a, b, gcd):
    def check_is_cd(d):
        return (a % d == 0) and (b % d == 0)

    if not check_is_cd(gcd):
        return False

    for i in range(gcd + 1, min(a, b) + 1):
        if check_is_cd(i):
            return False

    return True


def test(gcd_finder):
    n_test = 50
    bounds = (-150, 150)
    for _ in range(n_test):
        a, b = randint(*bounds), randint(*bounds)
        gcd = gcd_finder(a, b)
        assert check_is_gcd(a, b, gcd)


if __name__ == '__main__':
    test(gcd_finder=recursive)
    # test(gcd_finder=euclidian)
