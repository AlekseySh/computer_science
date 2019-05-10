from enum import Enum


class Node:

    def __init__(self,
                 val,
                 left=None,
                 right=None,
                 parent=None
                 ):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def has_no_child(self):
        return not self.has_left_child() and \
               not self.has_right_child()

    def has_one_child(self):
        return (self.has_left_child() +
                self.has_right_child()) == 1

    def has_both_children(self):
        return self.has_left_child() and \
               self.has_right_child()

    def __str__(self):
        return str(self.val)


class TraverseMode(Enum):
    Prefix = 0
    Infix = 1
    Postfix = 2


class BinSearchTree:

    def __init__(self):
        self._len = 0
        self.root = Node(None)

    def __len__(self):
        return self._len

    def remove(self, val):
        if not self:
            return

        elif len(self) == 1:
            del self.root
            self._len -= 1

        else:
            self._rm_step(self.root, val)

    def _rm_step(self, cur_node, val):
        if cur_node.val < val:
            self._rm_step(cur_node.right, val)

        elif cur_node.val > val:
            self._rm_step(cur_node.left, val)

        # cur_node.val == val
        else:
            if cur_node.has_no_child():
                if cur_node.parent.val < val:
                    cur_node.parent.right = None
                else:
                    cur_node.parent.left = None
                del cur_node
                self._len -= 1

            elif cur_node.has_one_child():
                child = cur_node.left if cur_node.has_left_child() else cur_node.right
                cur_node.val = child.val
                cur_node.left = child.left
                cur_node.right = child.right
                del child
                self._len -= 1

            # has both children
            else:
                if cur_node.right.left is None:
                    child_right = cur_node.right
                    cur_node.val = child_right.val
                    cur_node.right = child_right.right
                    del child_right
                    self._len -= 1

                else:
                    most_left = cur_node.right.left
                    while most_left.left is not None:
                        most_left = most_left.left

                    cur_node.val = most_left.val
                    self._rm_step(most_left, most_left.val)

    def set_root(self, val):
        self.root = Node(val)

    def find(self, val):
        if not self:
            return
        else:
            return self._find_step(self.root, val)

    def _find_step(self, cur_node, val):
        if val < cur_node.val:
            if cur_node.has_left_child():
                return self._find_step(cur_node.left, val)
            else:
                return

        elif val > cur_node.val:
            if cur_node.has_right_child():
                return self._find_step(cur_node.right, val)
            else:
                return

        else:  # case: val == cur_node.val
            return cur_node.val

    def add(self, val):
        if self:
            self._add_step(self.root, val)
        else:
            self.set_root(val)
        self._len += 1

    def _add_step(self, cur_node, val):
        if cur_node.val <= val:
            if cur_node.has_right_child():
                self._add_step(cur_node.right, val)
            else:
                cur_node.right = Node(val)
                cur_node.right.parent = cur_node

        else:
            if cur_node.has_left_child():
                self._add_step(cur_node.left, val)
            else:
                cur_node.left = Node(val)
                cur_node.left.parent = cur_node

    def traverse(self, mode):
        print(mode)
        if self:
            self._traverse_step(self.root, mode)
        else:
            return

    def _traverse_step(self, cur_node, mode):
        def left_call():
            if cur_node.has_left_child():
                self._traverse_step(cur_node.left, mode)

        def right_call():
            if cur_node.has_right_child():
                self._traverse_step(cur_node.right, mode)

        def root_call():
            print(cur_node)

        if mode == TraverseMode.Infix:
            left_call()
            root_call()
            right_call()

        elif mode == TraverseMode.Prefix:
            root_call()
            left_call()
            right_call()

        elif mode == TraverseMode.Postfix:
            left_call()
            right_call()
            root_call()

        else:
            ValueError(f'Undefined traverse mode {mode}.')


def bst_check():
    bst = BinSearchTree()
    bst.add(8)
    bst.add(3)
    bst.add(10)
    bst.add(1)
    bst.add(6)
    bst.add(4)
    bst.add(7)
    bst.add(14)
    bst.add(13)

    bst.remove(8)

    bst.traverse(TraverseMode.Infix)
    print()
    bst.traverse(TraverseMode.Postfix)
    print()
    bst.traverse(TraverseMode.Prefix)

    print('\nfind')
    print(bst.find(val=8))


if __name__ == '__main__':
    bst_check()
