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

    def no_childs(self):
        return not self.has_left_child() and \
               not self.has_right_child()

    def has_one_child(self):
        return self.has_right_child() \
               + self.has_right_child() == 1

    def __str__(self):
        return str(self.val)


class TraverseMode(Enum):
    Prefix = 0
    Infix = 1
    Postfix = 2


class BinSearchTree:

    def __init__(self):
        self.len = 0
        self.root = Node(None)

    def __len__(self):
        return self.len

    def remove(self, val):
        if not self:
            return
        else:
            self.rm_step(self.root, val)

    def rm_step(self, cur_node, val):
        if cur_node.val < val:
            self.rm_step(cur_node.right, val)

        elif cur_node.val > val:
            self.rm_step(cur_node.left, val)

        # cur_node.val == val
        else:
            if cur_node.no_childs():
                if cur_node.parent.val <= val:
                    cur_node.parent.left = None
                else:
                    cur_node.parent.right = None
                del cur_node

            elif cur_node.has_one_child():
                1

            # has both childs
            else:
                1

    def set_root(self, val):
        self.root = Node(val)

    def find(self, val):
        pass

    def add(self, val):
        if self:
            self.add_step(self.root, val)
        else:
            self.set_root(val)
        self.len += 1

    def add_step(self, cur_node, val):
        if cur_node.val <= val:
            if cur_node.has_right_child():
                self.add_step(cur_node.right, val)
            else:
                cur_node.right = Node(val)
                cur_node.right.parent = cur_node

        else:
            if cur_node.has_left_child():
                self.add_step(cur_node.left, val)
            else:
                cur_node.left = Node(val)
                cur_node.left.parent = cur_node

    def traverse(self, mode):
        print(mode)
        if self:
            self.traverse_step(self.root, mode)
        else:
            return

    def traverse_step(self, cur_node, mode):
        def left_call():
            if cur_node.has_left_child():
                self.traverse_step(cur_node.left, mode)

        def right_call():
            if cur_node.has_right_child():
                self.traverse_step(cur_node.right, mode)

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

    bst.remove(10)

    bst.traverse(TraverseMode.Infix)
    print()
    bst.traverse(TraverseMode.Postfix)
    print()
    bst.traverse(TraverseMode.Prefix)


if __name__ == '__main__':
    bst_check()
