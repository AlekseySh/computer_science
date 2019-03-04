import numpy as np

from structures.hash_map import HashMap
from structures.list import List
from structures.queue import Queue


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

    i_to_names = HashMap()
    i_to_names[0] = '1'
    i_to_names[1] = '2'
    i_to_names[2] = '3'
    i_to_names[3] = '4'
    i_to_names[4] = '6'
    i_to_names[5] = '12'

    edge_list = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 4),
        (3, 5),
        (4, 5)
    ]
    return edge_list, i_to_names


def get_sample1_graph():
    i_to_names = HashMap()
    for i in range(0, 9):
        i_to_names[i] = str(i + 1)

    # todo
    return 1


# Algos

def dfs(adj_list):
    visited, ii_order = List(), List()

    def step(idx: int):
        if idx in visited:
            return
        else:
            visited.append(idx)
            ii_order.append(idx)
            for j in adj_list[idx]:
                step(idx=j)

    step(idx=0)
    return ii_order


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
    edge_list, i_to_names = get_divisibility_graph()
    adj_list = edge_list_to_adj_list(edge_list)

    print(edge_list_to_adj_mat(edge_list))

    ii_order = bfs(adj_list)
    for i in ii_order:
        print(i_to_names[i])


def search2():
    get_sample1_graph()
    # todo


if __name__ == '__main__':
    search()
    search2()
