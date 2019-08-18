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

    def has_child(self):
        return not self.has_no_child()

    def __str__(self):
        return str(self.val)


class ExtNode(Node):

    def get_children(self):
        children = [c for c in (self.left, self.right) if c is not None]
        return children

    def get_grandchildren(self):
        granchildren = []

        if self.has_child():
            for node in self.get_children():
                granchildren.extend(node.get_children())

        return granchildren

    def set_children(self, left=None, right=None):
        if left is not None:
            self.left = left
            self.left.parent = self

        if right is not None:
            self.right = right
            self.right.parent = self


def get_sample_tree():
    # level 1
    node1 = ExtNode(1)

    # level 2
    node2 = ExtNode(2)
    node3 = ExtNode(3)

    # level3
    node4 = ExtNode(4)
    node5 = ExtNode(5)
    node6 = ExtNode(6)
    node7 = ExtNode(7)

    # level 4
    node8 = ExtNode(8)

    # level 5
    node9 = ExtNode(9)

    # links
    node1.set_children(node2, node3)
    node2.set_children(node4, node5)
    node3.set_children(node6, node7)
    node7.set_children(node8)
    node8.set_children(node9)

    independent_size = 6
    return node1, independent_size


if __name__ == '__main__':
    print(get_sample_tree().get_children()[1])
