from collections import deque

from list import List


class Queue:

    def __init__(self):
        self.max_size = 100
        self._list = List()

    def enqueue(self, value):
        # add element to end of queue
        self._list.append(value)

        if len(self) > self.max_size:
            raise Exception('Queue overflow!')

    def dequeue(self):
        # get and remove first element of queue
        val = self._list[0]
        del self._list[0]
        return val

    def __contains__(self, val):
        if len(self) == 0:
            return False

        for cur_val in self._list:
            if (cur_val is not None) and (cur_val == val):
                return True
        return False

    def __len__(self):
        return len(self._list)

    def __str__(self):
        text = '< '
        while len(self) > 0:
            text += str(self.dequeue())
            text += ' '
        return text


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    q.enqueue(150)

    print('my')
    print(q)

    d = deque()
    d.append(10)
    d.append(20)
    d.append(40)
    d.append(50)
    d.popleft()
    d.append(150)

    print('default')
    print(d)
