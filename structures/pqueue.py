from enum import Enum

import numpy as np

from structures.bin_heap import BinHeap

__all__ = ['get_pqueue', 'QueueBase']


class QueueBase(Enum):
    ARR = 1
    ARR_SORT = 2
    HEAP = 3


def get_pqueue(base=QueueBase.HEAP):
    if base == QueueBase.HEAP:
        pqueue = PQueueHeap()

    elif base == QueueBase.ARR_SORT:
        pqueue = PQueueArrSort()

    elif base == QueueBase.ARR:
        pqueue = PQueueArr()

    else:
        raise ValueError(f'Unexpected base for queue: {base}')

    return pqueue


class PQueue:

    def __init__(self):
        pass

    def pop_max(self):
        raise NotImplementedError

    def add(self, val):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __str__(self):
        text = '< '
        while self:
            text += str(self.pop_max())
            text += ' '
        return text


class PQueueArr(PQueue):

    def __init__(self):
        super().__init__()
        self.arr = np.array([], np.int)

    def pop_max(self):
        i_max = self.arr.argmax()
        v_max = self.arr[i_max]
        self.arr = np.delete(self.arr, i_max)
        return v_max

    def add(self, val):
        self.arr = np.append(self.arr, val)

    def __len__(self):
        return len(self.arr)


class PQueueArrSort(PQueue):
    def __init__(self):
        super().__init__()
        self.arr = np.array([], np.int)

    def pop_max(self):
        i_max = len(self) - 1
        v_max = self.arr[i_max]
        self.arr = np.delete(self.arr, i_max)
        return v_max

    def add(self, val):
        if (not self) or (val >= self.arr[-1]):
            self.arr = np.append(self.arr, val)
            return

        # todo
        # it can be improved from O(n) to O(log(n)) with bin search
        for i in range(len(self)):
            if val <= self.arr[i]:
                self.arr = np.insert(self.arr, i, val)
                return

    def __len__(self):
        return len(self.arr)


class PQueueHeap(PQueue):

    def __init__(self):
        super().__init__()
        self.heap = BinHeap()

    def pop_max(self):
        return self.heap.pop_max()

    def add(self, val):
        self.heap.add(val)

    def __len__(self):
        return len(self.heap)


def usage(pqueue):
    pqueue.add(10)
    pqueue.add(20)
    pqueue.add(5)
    pqueue.add(40)
    pqueue.add(50)
    pqueue.pop_max()
    pqueue.add(49)
    pqueue.add(51)
    pqueue.add(10)
    pqueue.pop_max()
    pqueue.add(100)
    pqueue.add(10)
    pqueue.add(1)
    pqueue.pop_max()
    pqueue.add(10)
    pqueue.pop_max()
    pqueue.pop_max()
    print(pqueue)


def main():
    usage(get_pqueue(QueueBase.ARR))
    usage(get_pqueue(QueueBase.ARR_SORT))
    usage(get_pqueue(QueueBase.HEAP))


if __name__ == '__main__':
    main()
