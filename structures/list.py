__all__ = ['List']


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class List:

    def __init__(self):
        self.header = Node(val='header')
        self.last_node = self.header
        self.len = 0

    def append(self, val: object):
        self.last_node.next = Node(val)
        self.last_node = self.last_node.next
        self.len += 1
        return self

    def __delitem__(self, idx):
        idx = self._to_positive_idx(idx)
        prev_node = self.__get_prev_node(idx)
        next_node = self.__get_next_node(idx)
        prev_node.next = next_node

        if idx == self.len - 1:
            self.last_node = prev_node

        self.len -= 1

        return self

    def insert(self, val: object, idx: int):
        if idx < 0:
            idx = self._to_positive_idx(idx) + 1

        if idx == self.len:
            self.append(val)
        else:
            prev_node = self.__get_prev_node(idx)
            cur_node = prev_node.next
            prev_node.next = Node(val)
            prev_node.next.next = cur_node
            self.len += 1
        return self

    def reverse(self):
        if self.len in [0, 1]:
            return self

        prev_node = self.header.next
        cur_node = prev_node.next

        prev_node.next = None
        self.last_node = prev_node

        k = 0
        while True:

            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node

            if k == self.len - 2:
                break

            cur_node = next_node
            k += 1

        self.header.next = cur_node
        return self

    def _to_positive_idx(self, idx):
        if idx < 0:
            idx += self.len
        return idx

    def __get_prev_node(self, positive_idx):
        if positive_idx == 0:
            prev_node = self.header
        else:
            prev_node = self._get_node(positive_idx - 1)
        return prev_node

    def __get_next_node(self, positive_idx):
        if self.len == positive_idx + 1:
            next_node = None
        else:
            next_node = self._get_node(positive_idx + 1)
        return next_node

    def find(self, val):
        for i, cur_val in enumerate(self):
            if cur_val == val:
                return i
        return None

    def __len__(self):
        return self.len

    def __str__(self):
        ret = '['
        for i, val in enumerate(self):
            ret += str(val)
            if i < self.len - 1:
                ret += ', '
        ret += ']'
        return ret

    def _get_node(self, idx):
        idx = self._to_positive_idx(idx)

        if idx >= self.len:
            raise IndexError(f'Index {idx} out of range \
             for list with len {self.len}.')

        cur_node = self.header.next
        for _ in range(idx):
            cur_node = cur_node.next

        return cur_node

    def __getitem__(self, idx: int):
        return self._get_node(idx).val

    def __setitem__(self, idx, val):
        self._get_node(idx).val = val

    def __contains__(self, val):
        for cur_val in self:
            if cur_val == val:
                return True
        return False


if __name__ == '__main__':
    ll = List()
    ll.append(100)
    ll.append(200)
    ll.append(300)
    ll.append(400)
    ll.append(500)
    ll.append(600)
    ll.append(700)
    ll.append(800)

    ll.reverse()
    ll.append(30)

    ll[5] = 1

    print(800 in ll)

    print(ll)
