from list import List
from queue import Queue


class GraphNode:

    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.nexts = []

    def __str__(self):
        return str(self.val)


def get_divisibility_graph():
    # divisibility relation graph

    # https://ru.wikipedia.org/wiki/Ориентированный_граф#
    # /media/File:Divisors_12.svg

    node1 = GraphNode('1', idx=0)
    node2 = GraphNode('2', idx=1)
    node3 = GraphNode('3', idx=2)
    node4 = GraphNode('4', idx=3)
    node6 = GraphNode('6', idx=4)
    node12 = GraphNode('12', idx=5)

    node1.nexts = [node2, node3]
    node2.nexts = [node4, node6]
    node3.nexts = [node6]
    node4.nexts = [node12]
    node6.nexts = [node12]
    node12.nexts = []

    return node1


def get_another_graph():
    # https://studfiles.net/html/710/197/html_NWMgMuIzg5.QMJb/img-CGdkcL.png

    node1 = GraphNode('1', idx=0)

    node3 = GraphNode('3', idx=1)
    node4 = GraphNode('4', idx=2)

    node6 = GraphNode('6', idx=3)
    node2 = GraphNode('2', idx=4)
    node5 = GraphNode('5', idx=5)

    node7 = GraphNode('7', idx=6)
    node8 = GraphNode('8', idx=7)

    node9 = GraphNode('9', idx=8)

    node1.nexts = [node3, node4]
    node3.nexts = [node6, node2]
    node4.nexts = [node5]
    node5.nexts = [node7, node8]
    node6.nexts = [node7]
    node7.nexts = [node9]
    node8.nexts = [node7]
    node9.nexts = []
    return node1


# DFS
def get_all_values_dfs(head):
    visited_ids, visited_vals = List(), List()
    dfs(head, visited_ids, visited_vals)
    return visited_vals


def dfs(node, visited_ids, visited_vals):
    # depth first algorithm
    if node.idx not in visited_ids:
        visited_ids.append(node.idx)
        visited_vals.append(node.val)
        for node in node.nexts:
            dfs(node, visited_ids, visited_vals)


# BFS
def get_all_values_bfs(head):
    visited_ids, visited_vals = List(), List()
    queue = Queue()

    queue.enqueue(head)
    visited_ids.append(head.idx)
    visited_vals.append(head.val)

    bfs(queue, visited_ids, visited_vals)
    return visited_vals


def bfs(queue, visited_ids, visited_vals):
    # breadth first algorithm

    if not queue:
        return

    node = queue.dequeue()

    for next_node in node.nexts:
        if next_node.idx not in visited_ids:
            queue.enqueue(next_node)
            visited_ids.append(next_node.idx)
            visited_vals.append(next_node.val)

    bfs(queue, visited_ids, visited_vals)
    return visited_vals


if __name__ == '__main__':
    head_node = get_divisibility_graph()
    vals = get_all_values_dfs(head_node)

    print('\nValues:')
    print(vals)
