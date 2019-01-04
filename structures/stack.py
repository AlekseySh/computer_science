from list import List


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

    def __len__(self):
        return len(self._list)

    def __str__(self):
        text = '> '
        i = 0
        while len(self):
            text += self.pop()
            if i <= len(self):
                text += ', '
            i += 1
        text += ' >'
        return text


if __name__ == '__main__':
    stack = Stack()
    stack.push('1')
    stack.push('2')
    stack.push('3')
    stack.push('4')
    stack.pop()

    print(stack)
