from structures.list import List

__all__ = ['Queue']


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

    print(q)
