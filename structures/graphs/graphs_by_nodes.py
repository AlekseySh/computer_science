from structures.list import List
from structures.queue import Queue


class Node:

    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.nexts = []

    def __str__(self):
        return str(self.val)


def get_divisibility_graph():
    node1 = Node('1', idx=0)
    node2 = Node('2', idx=1)
    node3 = Node('3', idx=2)
    node4 = Node('4', idx=3)
    node6 = Node('6', idx=4)
    node12 = Node('12', idx=5)

    node1.nexts = [node2, node3]
    node2.nexts = [node4, node6]
    node3.nexts = [node6]
    node4.nexts = [node12]
    node6.nexts = [node12]
    node12.nexts = []

    return node1


def get_example_graph():
    # https://studfiles.net/html/710/197/
    # html_NWMgMuIzg5.QMJb/img-CGdkcL.png

    node1 = Node('1', idx=0)

    node3 = Node('3', idx=1)
    node4 = Node('4', idx=2)

    node6 = Node('6', idx=3)
    node2 = Node('2', idx=4)
    node5 = Node('5', idx=5)

    node7 = Node('7', idx=6)
    node8 = Node('8', idx=7)

    node9 = Node('9', idx=8)

    node1.nexts = [node3, node4]
    node3.nexts = [node6, node2]
    node4.nexts = [node5]
    node5.nexts = [node7, node8]
    node6.nexts = [node7]
    node7.nexts = [node9]
    node8.nexts = [node7]
    node9.nexts = []
    return node1


# DFS (depth first algorithm)
def dfs(head):
    visited_ids, visited_vals = set(), List()

    def step(node):
        if node.idx not in visited_ids:
            visited_ids.add(node.idx)
            visited_vals.append(node.val)
            for node in node.nexts:
                step(node)

    step(head)
    return visited_vals


# BFS (breadth first algorithm)
def bfs(head):
    visited_ids, visited_vals = set(), List()

    queue = Queue()
    queue.enqueue(head)

    visited_ids.add(head.idx)
    visited_vals.append(head.val)

    def step():
        if not queue:
            return

        node = queue.dequeue()

        for next_node in node.nexts:
            if next_node.idx not in visited_ids:
                queue.enqueue(next_node)
                visited_ids.add(next_node.idx)
                visited_vals.append(next_node.val)

        step()
        return visited_vals

    step()
    return visited_vals


if __name__ == '__main__':
    head_node = get_example_graph()
    print(dfs(head_node))
    print(bfs(head_node))
