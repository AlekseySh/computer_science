import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from structures.hash_map import HashMap
from structures.list import List
from structures.queue import Queue
from structures.stack import Stack


# Transforms

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


# Samples

def get_divisibility_graph():
    # https://ru.wikipedia.org/wiki/Ориентированный_граф#
    # /media/File:Divisors_12.svg

    labels = HashMap()
    labels[0] = '1'
    labels[1] = '2'
    labels[2] = '3'
    labels[3] = '4'
    labels[4] = '6'
    labels[5] = '12'

    edge_list = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 4),
        (3, 5),
        (4, 5)
    ]
    return edge_list, labels


# Algos
def dfs_step(idx,
             visited,
             ii_order,
             adj_list,
             ii_stack=None
             ):
    if idx in visited:
        return
    else:
        visited.append(idx)
        ii_order.append(idx)

        for j in adj_list[idx]:
            dfs_step(j,
                     visited,
                     ii_order,
                     adj_list,
                     ii_stack
                     )

    if ii_stack is not None:
        ii_stack.push(idx)


def dfs(adj_list):
    visited, ii_order = List(), List()
    dfs_step(0, visited, ii_order, adj_list)
    return ii_order


def top_sort(adj_list):
    visited, ii_order, ii_sort = List(), List(), List()
    stack = Stack()

    dfs_step(0, visited, ii_order, adj_list, stack)

    sorted_ids = stack.to_list()
    return sorted_ids


def bfs(adj_list):
    visited, ii_order = List(), List()
    queue = Queue()

    i_start = 0
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

def search():
    edge_list, i_to_labels = get_divisibility_graph()
    adj_list = edge_list_to_adj_list(edge_list)

    bfs_labels = [i_to_labels[i] for i in bfs(adj_list)]
    print(f'BFS order:\n {bfs_labels}')

    dfs_labels = [i_to_labels[i] for i in dfs(adj_list)]
    print(f'DFS order:\n {dfs_labels}')


# visualisation
def draw(edge_list, labels):
    g = nx.DiGraph()
    g.add_edges_from(edge_list)
    pos = nx.spring_layout(g)

    plt.figure()
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(
        g, pos, labels=labels, font_size=20)
    plt.show()


def top_sort_check():
    edge_list, labels = get_divisibility_graph()
    adj_list = edge_list_to_adj_list(edge_list)

    ii_sort = top_sort(adj_list)

    g = nx.DiGraph()
    g.add_edges_from(edge_list)
    ii_sort_lib = list(nx.topological_sort(g))

    print(f'Topological sort: {ii_sort_lib} (lib).')
    print(f'Topological sort: {ii_sort} (our).')


if __name__ == '__main__':
    search()
    top_sort_check()
