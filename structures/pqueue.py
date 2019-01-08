from enum import Enum

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


class PQueueArr(PQueue):

    def __init__(self):
        super().__init__()
        pass

    def pop_max(self):
        raise NotImplementedError

    def add(self, val):
        raise NotImplementedError


class PQueueArrSort(PQueue):
    def __init__(self):
        super().__init__()
        pass

    def pop_max(self):
        raise NotImplementedError

    def add(self, val):
        raise NotImplementedError


class PQueueHeap(PQueue):

    def __init__(self):
        super().__init__()
        pass

    def pop_max(self):
        raise NotImplementedError

    def add(self, val):
        raise NotImplementedError


def main():
    pq_arr = get_pqueue(QueueBase.ARR)
    pq_arr_sort = get_pqueue(QueueBase.ARR_SORT)
    pq_heap = get_pqueue(QueueBase.HEAP)
    return 0


if __name__ == '__main__':
    main()
