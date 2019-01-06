from math import log2, ceil

from algorithms.sorting.test import test

__all__ = ['merge_sort_iterative', 'merge_sort_recursively', 'main']


def merge(a, b):
    # assume, that a and b are sorted
    n_a, n_b = len(a), len(b)
    i_a, i_b = 0, 0

    ab = []
    while (i_a < n_a) and (i_b < n_b):
        if a[i_a] <= b[i_b]:
            ab.append(a[i_a])
            i_a += 1

        else:
            ab.append(b[i_b])
            i_b += 1

    # now a or b guaranted empty, therefore, only one
    # of the cycles will be executed.
    while i_b < n_b:
        ab.append(b[i_b])
        i_b += 1

    while i_a < n_a:
        ab.append(a[i_a])
        i_a += 1

    return ab


def merge_inplace(x, left, mid, right):
    a = x[left: mid]  # copy here: O(n) memory
    b = x[mid: right]
    merged_ab = merge(a, b)
    for i, ab in enumerate(merged_ab):
        x[left + i] = ab


def _merge_sort_recursively(x, left, right):
    if left + 1 >= right:
        return

    mid = (left + right) // 2
    _merge_sort_recursively(x, left, mid)
    _merge_sort_recursively(x, mid, right)
    merge_inplace(x, left, mid, right)


def merge_sort_recursively(x):
    _merge_sort_recursively(x, 0, len(x))


def merge_sort_iterative(x):
    n = len(x)

    if n <= 1:
        return

    n_levels = ceil(log2(n)) + 1
    for section in [2 ** i for i in range(1, n_levels)]:

        n_sections = ceil(n // section) + 1
        for left in [j * section for j in range(0, n_sections)]:
            mid = left + section // 2
            right = min(left + section, n)
            merge_inplace(x, left, mid, right)


def main():
    test(sort_func=merge_sort_iterative)
    test(sort_func=merge_sort_recursively)
    print('Merge-sort passed tests!')


if __name__ == '__main__':
    main()
