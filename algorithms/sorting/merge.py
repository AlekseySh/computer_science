"""
Based on:
https://neerc.ifmo.ru/wiki/index.php?title=Сортировка_слиянием
"""
from math import log2, ceil

__all__ = ['merge_sort_iterative', 'merge_sort_recursively']


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
    #  of the cycles will be executed.
    while i_b < n_b:
        ab.append(b[i_b])
        i_b += 1

    while i_a < n_a:
        ab.append(a[i_a])
        i_a += 1

    return ab


def merge_inplace(x, left, mid, right):
    a = x[left: mid]
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
    if len(x) > 1:
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


if __name__ == '__main__':
    inp = [3, 7, 3, 5, 15, 1, 2, 4, 0, 15, 16, 19, 20, 1]
    merge_sort_iterative(inp)
    print(inp)
