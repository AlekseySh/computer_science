class BiNode:

    def __init__(self, val):
        self.val = val
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        prev_str = self.prev_node.val if self.prev_node is not None else 'none'
        next_str = self.next_node.val if self.next_node is not None else 'none'
        text = f'{prev_str} <- [{self.val}] -> {next_str}'
        return text


class BiList:

    def __init__(self):
        self.header = BiNode('header')
        self.last_node = self.header
        self.len = 0

    def append(self, val):
        self.last_node.next_node = BiNode(val)
        self.last_node.next_node.prev_node = self.last_node
        self.last_node = self.last_node.next_node
        self.len += 1

    def __delitem__(self, idx):
        cur_node = self[idx]
        next_node = cur_node.next_node
        prev_node = cur_node.prev_node
        prev_node.next_node = next_node
        next_node.prev_node = prev_node
        self.len -= 1
        del cur_node

    def __setitem__(self, idx, val):
        self[idx].val = val

    def reverse(self):
        cur_node = self.last_node
        k = 0
        while True:
            prev_node = cur_node.prev_node
            next_node = cur_node.next_node
            cur_node.next_node = prev_node
            cur_node.prev_node = next_node

            if k == self.len - 1:
                break

            cur_node = prev_node
            k += 1

        self.header.next_node = self.last_node
        self.last_node.prev_node = self.header
        self.last_node = cur_node

    def __len__(self):
        return self.len

    def __str__(self):
        text = f'[{self.header}, '
        node = self.header.next_node
        for k in range(self.len):
            text += str(node)
            node = node.next_node
            text += ', ' if k != self.len - 1 else ''
        text += ']'
        return text

    def __getitem__(self, idx):
        if (idx > self.len - 1) or (idx < 0):
            raise IndexError

        cur_node = self.header
        k = 0
        while k <= idx:
            cur_node = cur_node.next_node
            k += 1
        return cur_node


if __name__ == '__main__':
    ll = BiList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    print(ll)
    ll[0] = 1000
    ll.reverse()
    print(ll)
