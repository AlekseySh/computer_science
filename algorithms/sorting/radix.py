import numpy as np

from algorithms.sorting.test import test

__all__ = ['radix_sort']


def get_ndigit_value(num, n_digit):
    # get value of n-th number digit
    v_digit = (num % (10 ** (n_digit + 1))) // (10 ** n_digit)
    assert 0 <= v_digit <= 9
    return v_digit


def count_digits(num):
    # get count of non-zero digits in number
    n_digit = 0
    while True:
        ratio = num // (10 ** n_digit)
        n_digit += 1

        if ratio < 10:
            return n_digit - 1


def counting_sort_by_digit(x, n_digit):
    counts = np.zeros(10, dtype=np.int)

    for num in x:
        v_digit = get_ndigit_value(num, n_digit)
        counts[v_digit] += 1

    new_ids = np.insert(np.cumsum(counts[:-1]), 0, 0)

    x_sorted = [None for _ in x]
    for num in x:
        digit_v = get_ndigit_value(num, n_digit)
        new_idx = new_ids[digit_v]
        new_ids[digit_v] += 1

        x_sorted[new_idx] = num

    return x_sorted


def radix_sort(x):
    # work only for integer inputs
    if not x:
        return []

    n_digit_max = count_digits(max(x))

    for n_digit in range(0, n_digit_max + 1):
        x = counting_sort_by_digit(x, n_digit)

    return x


def main():
    test(sort_func=radix_sort, inplace_sort=False)
    print('Radix-sort passed tests!')


if __name__ == '__main__':
    main()
