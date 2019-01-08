__all__ = ['BiList']


class BiNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)


class BiList:

    def __init__(self):
        self.header = BiNode('header')
        self.last_node = self.header
        self.len = 0

    def append(self, val):
        self.last_node.next = BiNode(val)
        self.last_node.next.prev = self.last_node
        self.last_node = self.last_node.next
        self.len += 1

    def __delitem__(self, idx):
        cur_node = self[idx]
        next_node = cur_node.next
        prev_node = cur_node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

        if idx == self.len - 1:
            self.last_node = prev_node

        self.len -= 1

        del cur_node

    def __setitem__(self, idx, val):
        self[idx].val = val

    def reverse(self):
        cur_node = self.last_node
        k = 0
        while True:
            prev_node = cur_node.prev
            next_node = cur_node.next
            cur_node.next = prev_node
            cur_node.prev = next_node

            if k == self.len - 1:
                break

            cur_node = prev_node
            k += 1

        self.header.next = self.last_node
        self.last_node.prev = self.header
        self.last_node = cur_node
        self.last_node.next = None

    def __len__(self):
        return self.len

    def __str__(self, f_str=None):
        if f_str is None:
            f_str = str

        text = '['
        node = self.header.next
        for k in range(self.len):
            text += f_str(node)
            node = node.next
            text += ', ' if k != self.len - 1 else ''
        text += ']'
        return text

    def print_structure(self):

        def f_str_neighbors(node):
            prev_str = node.prev.val if node.prev is not None else 'none'
            next_str = node.next.val if node.next is not None else 'none'
            text = f'{prev_str} <- [{node.val}] -> {next_str}'
            return text

        print(self.__str__(f_str=f_str_neighbors))

    def __getitem__(self, idx):
        if (idx > self.len - 1) or (idx < 0):
            raise IndexError

        cur_node = self.header
        k = 0
        while k <= idx:
            cur_node = cur_node.next
            k += 1
        return cur_node


if __name__ == '__main__':
    ll = BiList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll[0] = -1
    ll.reverse()
    ll.append(10)

    print(ll)
    ll.print_structure()
