__all__ = ['BinHeap']


class BinHeap:

    def __init__(self, values):
        # values should be default or custom list
        self.h = values
        self.n = len(values)

    def __len__(self):
        return self.n

    def build_heap(self):
        for i in range(self.n // 2, -1, -1):
            self.heapify(i)

    def heapify(self, idx):
        i_left = BinHeap.left(idx)
        i_right = BinHeap.right(idx)

        i_max = idx

        if i_left < self.n and self.h[i_left] > self.h[idx]:
            i_max = i_left

        if i_right < self.n and self.h[i_right] > self.h[i_max]:
            i_max = i_right

        if i_max != idx:
            self.h[idx], self.h[i_max] = self.h[i_max], self.h[idx]
            self.heapify(i_max)

    def inplace_sort(self):
        for i in range(1, self.n):
            self.h[0], self.h[-i] = self.h[-i], self.h[0]
            self.n -= 1
            self.heapify(0)

        self.n = len(self.h)

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def __str__(self):
        return str(self.h)


if __name__ == '__main__':
    ll = [16, 11, 9, 10, 5, 6, 3, 4, 0, 1, 1, 2]
    heap = BinHeap(ll)
    heap.build_heap()
    print(heap)
    print()

    heap.inplace_sort()
    print()
    print(heap)
