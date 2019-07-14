import numpy as np

from structures.bin_heap import BinHeap
from structures.graphs.graphs import adjacency_mat_to_list, adj_list_to_edge_list


def get_example_graph():
    mat = np.zeros((8, 8), dtype=np.float)
    mat[0, 2] = mat[2, 0] = 2
    mat[2, 3] = mat[3, 2] = 3
    mat[3, 4] = mat[4, 3] = 1
    mat[0, 1] = mat[1, 0] = 1
    mat[1, 5] = mat[5, 1] = 2
    mat[4, 5] = mat[5, 4] = 8
    mat[1, 2] = mat[2, 1] = 1
    mat[1, 3] = mat[3, 1] = 1
    mat[3, 5] = mat[5, 3] = 4
    mat[6, 7] = mat[7, 6] = 1
    return mat


def fold_bellman(graph_mat, s_node):
    adj_list = adjacency_mat_to_list(graph_mat)
    edge_list = adj_list_to_edge_list(adj_list)
    n = graph_mat.shape[0]

    d = np.repeat(np.inf, n)
    d[s_node] = 0

    for k in range(n):
        for j, i in edge_list:

            if d[i] > d[j] + graph_mat[j, i]:
                d[i] = d[j] + graph_mat[j, i]

            i, j = j, i
            if d[i] > d[j] + graph_mat[j, i]:
                d[i] = d[j] + graph_mat[j, i]

    print('\nFold bellman algorithm')
    print(f'Dists from {s_node} to other nodes:\n{d}')
    return d


class DijkstraNode:

    def __init__(self, ind, dist):
        self.ind = ind
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist

    def __gt__(self, other):
        return self.dist > other.dist

    def __eq__(self, other):
        return self.dist == other.dist


def modify_heap(heap, ind, new_dist):
    # todo: speed up
    for item in heap.h:
        if item.ind == ind:
            item.dist = new_dist
    heap.build_heap()


def dijkstra(graph_mat, s_node):
    adj_list = adjacency_mat_to_list(graph_mat)
    n = graph_mat.shape[0]

    d = np.array([DijkstraNode(i, np.inf) for i in range(n)])
    d[s_node].dist = 0

    heap = BinHeap()
    for i, dn in enumerate(d):
        heap.add(DijkstraNode(ind=dn.ind, dist=-dn.dist))

    visited = set()

    while heap:
        i = heap.pop_max().ind

        for j in adj_list[i]:

            if j in visited:
                continue

            pivot = d[i].dist + graph_mat[j, i]
            if d[j].dist > pivot:
                d[j].dist = pivot
                modify_heap(heap, j, -pivot)

        visited.add(i)

    d = [item.dist for item in d]

    print('\nDijkstra algorithm:')
    print(f'Dists from {s_node} to other nodes:\n{d}')
    return d


def run_test():
    graph_mat, s_node = get_example_graph(), 0

    dists_fb = fold_bellman(graph_mat, s_node=s_node)
    dists_d = dijkstra(graph_mat, s_node=s_node)

    assert np.array_equal(dists_fb, dists_d), \
        f'\n{dists_fb}\n{dists_d}'


if __name__ == '__main__':
    run_test()
