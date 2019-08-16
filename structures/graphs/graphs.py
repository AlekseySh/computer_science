import warnings

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from structures.hash_map import HashMap
from structures.list import List
from structures.queue import Queue
from structures.stack import Stack


# Converters

def adjacency_mat_to_list(adj_mat):
    adj_list = List()
    for inds in adj_mat:
        adj_list.append(np.nonzero(inds)[0].tolist())
    return adj_list


def edge_list_to_adj_mat(edge_list):
    edges = {idx for edge in edge_list for idx in edge}
    n_v = len(edges)

    adj_mat = np.zeros([n_v, n_v], dtype=np.int)
    for edge in edge_list:
        adj_mat[edge[0], edge[1]] = True
    return adj_mat


def edge_list_to_adj_list(edge_list):
    adj_mat = edge_list_to_adj_mat(edge_list)
    adj_list = adjacency_mat_to_list(adj_mat)
    return adj_list


def adj_list_to_edge_list(adj_list):
    edge_list = []
    for u, v_nodes in enumerate(adj_list):
        for v in v_nodes:
            edge = sorted((u, v))
            if edge not in edge_list:
                edge_list.append(edge)
    return edge_list


# Samples

def get_divisibility_graph():
    # https://ru.wikipedia.org/wiki/Ориентированный_граф#
    # /media/File:Divisors_12.svg

    labels = HashMap()
    labels[1] = '1'
    labels[0] = '2'
    labels[2] = '3'
    labels[3] = '4'
    labels[4] = '6'
    labels[5] = '12'

    edge_list = [
        (1, 0),
        (1, 2),
        (0, 3),
        (0, 4),
        (2, 4),
        (3, 5),
        (4, 5)
    ]
    return edge_list, labels


# Algos

def dfs(adj_list, ii_start, stack=None):
    visited, ii_order = List(), List()

    def step(idx):

        if idx in visited:
            return

        else:
            visited.append(idx)
            ii_order.append(idx)

            for j in adj_list[idx]:
                step(j)

        if stack is not None:
            stack.push(idx)

    for node_idx in ii_start:
        step(node_idx)

    return ii_order


def top_sort(adj_list):
    stack = Stack()
    dfs(adj_list, stack=stack, ii_start=list(range(len(adj_list))))
    sorted_ids = stack.to_list()
    return sorted_ids


def bfs(adj_list, i_start=0):
    visited, ii_order = List(), List()
    queue = Queue()

    queue.enqueue(i_start)
    visited.append(i_start)
    ii_order.append(i_start)

    def step():
        if not queue:
            return
        else:
            i = queue.dequeue()
            for j in adj_list[i]:
                if j not in visited:
                    visited.append(j)
                    ii_order.append(j)
                    queue.enqueue(j)
            step()

    step()
    return ii_order


# Examples

def search_check():
    edge_list, i_to_labels = get_divisibility_graph()
    adj_list = edge_list_to_adj_list(edge_list)

    i_start = 0

    bfs_ii = bfs(adj_list, i_start=i_start)
    bfs_labels = [i_to_labels[i] for i in bfs_ii]
    print(f'BFS from [{i_start}]:\n {bfs_labels}\n')

    dfs_ii = dfs(adj_list, ii_start=[i_start])
    dfs_labels = [i_to_labels[i] for i in dfs_ii]
    print(f'DFS from [{i_start}]:\n {dfs_labels}\n')

    assert set(dfs_ii) == set(bfs_ii), \
        'Sets of reachable nodes must be the same.'


# visualisation
def draw(edge_list, labels):
    warnings.filterwarnings("ignore")

    labels_str = {key: f'{val} [{key}]' for key, val in labels.items()}

    g = nx.DiGraph()
    g.add_edges_from(edge_list)
    pos = nx.spring_layout(g)

    plt.figure()
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(
        g, pos, labels=labels_str, font_size=20)
    plt.axis('off')
    plt.show()


def top_sort_check():
    edge_list, i_to_labels = get_divisibility_graph()
    adj_list = edge_list_to_adj_list(edge_list)

    draw(edge_list, i_to_labels)

    # our
    ii_sort = top_sort(adj_list)
    labels_sort = [i_to_labels[i] for i in ii_sort]

    # lib
    g = nx.DiGraph()
    g.add_edges_from(edge_list)
    ii_sort_lib = list(nx.topological_sort(g))
    labels_sort_lib = [i_to_labels[i] for i in ii_sort_lib]

    print(f'Topological sort: {labels_sort_lib} (lib).')
    print(f'Topological sort: {labels_sort} (our).')


if __name__ == '__main__':
    search_check()
    top_sort_check()
