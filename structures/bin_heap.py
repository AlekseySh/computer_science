__all__ = ['BinHeap']


class BinHeap:

    def __init__(self):
        self.h = []
        self.n = 0

    @staticmethod
    def build_from_arr(values):
        # values should be default or custom list
        # but better use massive
        bin_heap = BinHeap()
        bin_heap.h = values
        bin_heap.n = len(bin_heap.h)
        bin_heap.build_heap()
        return bin_heap

    def add(self, val):
        self.h.append(val)
        self.n += 1

        i = self.n - 1

        def par(j): return BinHeap.parent(j)

        while (i > 0) and (self.h[i] > self.h[par(i)]):
            self.h[i], self.h[par(i)] = self.h[par(i)], self.h[i]
            i = par(i)

    def pop_max(self):
        v_max = self.h[0]
        self.h[0] = self.h[-1]
        del self.h[-1]
        self.n -= 1
        self.heapify(0)
        return v_max

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

    def __len__(self):
        return self.n

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return i // 2


def main():
    ll = [3, 22, 213, 400, 50, 312, 51, 11, 100, 10, 2]

    bin_heap = BinHeap()
    for l in ll:
        bin_heap.add(l)

    while bin_heap:
        print(bin_heap.pop_max())


if __name__ == '__main__':
    main()
