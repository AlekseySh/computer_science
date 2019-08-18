from structures.list import List

__all__ = ['Stack']


class Stack:

    def __init__(self):
        self.max_size = 100
        self._list = List()

    def push(self, val):
        self._list.insert(val, 0)

        if len(self) > self.max_size:
            raise Exception('Stack overflow!')

    def pop(self):
        val = self._list[0]
        del self._list[0]
        return val

    def peek(self):
        return self._list[0]

    def to_list(self):
        return self._list

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return str(self._list)

    def __contains__(self, val):
        return self._list.find(val) is not None


if __name__ == '__main__':
    stack = Stack()
    stack.push('1')
    stack.push('2')
    stack.push('3')
    stack.push(5)
    stack.push(5)
    stack.pop()

    print(stack)

    assert 5 in stack
    assert '1' in stack
    assert '5' not in stack
