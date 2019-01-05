from random import randint

from algorithms.sorting.merge import merge_sort_recursively, merge_sort_iterative


def test(sort_func,
         n_test=1000,
         size_bounds=(0, 10),
         val_bounds=(0, 10)
         ):
    for _ in range(n_test):
        x = [randint(*val_bounds) for _ in range(randint(*size_bounds))]

        x_for_default = x.copy()
        x_for_custom = x.copy()

        x_for_default.sort()  # default inplace sort
        sort_func(x_for_custom)  # custom inplace sort

        assert x_for_custom == x_for_default, \
            f'input: {x}, sorted: {x_for_custom}'


def main():
    test(sort_func=merge_sort_recursively)
    test(sort_func=merge_sort_iterative)
    print('All tests passed!')


if __name__ == '__main__':
    main()
