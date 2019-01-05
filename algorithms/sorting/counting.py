import numpy as np

from algorithms.sorting.test import test


def count_sort(x):
    if not x:
        return

    min_v, max_v = min(x), max(x)  # O(n)
    k = max_v - min_v + 1
    counts = np.zeros(k, dtype=np.int)  # O(k) memo

    for val in x:
        counts[val - min_v] += 1

    step = 0
    for val in range(min_v, max_v + 1):  # O(n)

        for _ in range(counts[val - min_v]):
            x[step] = val
            step += 1


def main():
    test(sort_func=count_sort)


if __name__ == '__main__':
    main()
