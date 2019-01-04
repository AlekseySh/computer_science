from random import randint

from algorithms.sorting.count import count_sort
from algorithms.sorting.heap import heap_sort
from algorithms.sorting.merge import merge_sort
from algorithms.sorting.number import number_sort
from algorithms.sorting.quick import quick_sort


def check_is_sorted(x):
    return x == sorted(x)


def test(sorter,
         n_test=10,
         size_bounds=(-100, 100),
         val_bounds=(0, 100)
         ):
    for _ in range(n_test):
        x = [randint(*val_bounds) for _ in range(randint(*size_bounds))]
        x_sorted = sorter(x)
        assert check_is_sorted(x_sorted)


def main():
    test(sorter=merge_sort)
    test(sorter=heap_sort)
    test(sorter=quick_sort)
    test(sorter=count_sort)
    test(sorter=number_sort)
    test(sorter=number_sort)
    print('All tests passed!')


if __name__ == '__main__':
    main()
