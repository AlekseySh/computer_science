from bisect import bisect_left
from random import randint


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

        if (last_nums[j - 1] < a) and (a < last_nums[j]):
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


def rand_ints(n, a, b):
    return [randint(a, b) for _ in range(n)]


def test():
    arr = rand_ints(20, 1, 15)
    subseq_ans = largest_incremental_subsequence(arr)

    print(arr)
    print(subseq_ans)


if __name__ == '__main__':
    test()
