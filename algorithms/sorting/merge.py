"""
Based on:
https://neerc.ifmo.ru/wiki/index.php?title=Сортировка_слиянием
"""


def merge(a, b):
    # assume, that a and b are sorted
    n_a, n_b = len(a), len(b)
    i_a, i_b = 0, 0

    result = []
    while (i_a < n_a) and (i_b < n_b):
        if a[i_a] <= b[i_b]:
            result.append(a[i_a])
            i_a += 1

        else:
            result.append(b[i_b])
            i_b += 1

    # now a or b guaranted empty, therefore, only one
    #  of the cycles will be executed.
    while i_b < n_b:
        result.append(b[i_b])
        i_b += 1

    while i_a < n_a:
        result.append(a[i_a])
        i_a += 1

    return result


def merge_inplace(x, left, mid, right):
    a = x[left: mid]
    b = x[mid: right + 1]
    for i, ab in enumerate(merge(a, b)):
        x[left + i] = ab
    return x


def merge_sort(x):
    return sorted(x)


def merge_sort_iterative():
    return sorted(x)


if __name__ == '__main__':
    inp = [13, 3, 8, 1, 15, 2, 3, 7, 4]
    print(merge_sort(inp))
