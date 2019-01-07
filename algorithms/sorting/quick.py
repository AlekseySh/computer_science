from algorithms.sorting.test import test
from structures.stack import Stack

__all__ = ['quick_sort_recursive']


def partitioning(x, i_left, i_last):
    i, j = i_left, i_last
    pivot = x[i_left]

    while i <= j:
        while x[i] < pivot:
            i += 1

        while x[j] > pivot:
            j -= 1

        if i <= j:
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1

    return i, j


def _quick_sort_recursive(x, i_left, i_last):
    if i_left >= i_last:
        return

    i, j = partitioning(x, i_left, i_last)
    _quick_sort_recursive(x, i_left, j)
    _quick_sort_recursive(x, i, i_last)


def quick_sort_recursive(x):
    _quick_sort_recursive(x, 0, len(x) - 1)


def quick_sort_iterative(x):
    i_left, i_right = 0, len(x) - 1

    stack = Stack()
    stack.push((i_left, i_right))

    while stack:

        i_left, i_right = stack.pop()

        if i_right <= i_left:
            continue

        i, j = partitioning(x, i_left, i_right)

        stack.push((i_left, j))
        stack.push((i, i_right))


def main():
    test(sort_func=quick_sort_recursive)
    test(sort_func=quick_sort_iterative)
    print('Quick-sort passed tests!')


if __name__ == '__main__':
    main()
