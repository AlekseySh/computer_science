from bisect import bisect_left

import numpy as np


def bin_search(arr, x0):
    i = bisect_left(a=arr, x=x0)
    if i != len(arr) and arr[i] == x0:
        return i
    raise ValueError


def largest_incremental_subsequence(arr):
    last_nums = [float('inf')] * len(arr)
    pos = [None] * len(arr)
    prev = [None] * (len(arr) - 1)
    length = 0

    last_nums[0] *= -1
    pos[0] = -1

    for i, a in enumerate(arr[:-1]):
        j = bisect_left(last_nums, a)
        if last_nums[j - 1] < a < last_nums[j]:
            last_nums[j] = a

            pos[j] = i
            prev[i] = pos[j - 1]
            length = max(length, j)

    p = pos[length]
    answer = []
    while p != - 1:
        answer.append(arr[p])
        p = prev[p]
    answer.reverse()
    return answer


def main():
    x = [0, 1, 0, 1, 2, 5, 6, 0, 6]
    subseq = largest_incremental_subsequence(x)
    print(subseq)
    assert np.all(np.diff(subseq) >= 0)


if __name__ == '__main__':
    main()
