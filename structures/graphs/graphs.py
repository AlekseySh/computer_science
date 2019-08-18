import numpy as np

from structures.hash_map import HashMap
from structures.list import List


# Converters

def adj_mat_to_adj_list(adj_mat):
    adj_list = List()
    for inds in adj_mat:
        adj_list.append(np.nonzero(inds)[0].tolist())

    return adj_list


def edge_list_to_adj_mat(edge_list):
    edges = {idx for edge in edge_list for idx in edge}
    n_v = len(edges)

    adj_mat = np.zeros([n_v, n_v], dtype=np.int)
    for (u, v) in edge_list:
        adj_mat[u, v] = True

    return adj_mat


def edge_list_to_adj_list(edge_list):
    adj_mat = edge_list_to_adj_mat(edge_list)
    adj_list = adj_mat_to_adj_list(adj_mat)
    return adj_list


def adj_list_to_edge_list(adj_list):
    edge_list = []
    for u, v_nodes in enumerate(adj_list):
        for v in v_nodes:
            if (u, v) not in edge_list:
                edge_list.append((u, v))

    return edge_list


# Examples


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


def get_divisibility_graph():
    i_to_label = HashMap()

    i_to_label[1] = '1'
    i_to_label[0] = '2'
    i_to_label[2] = '3'
    i_to_label[3] = '4'
    i_to_label[4] = '6'
    i_to_label[5] = '12'

    edge_list = [
        (1, 0),
        (1, 2),
        (0, 3),
        (0, 4),
        (2, 4),
        (3, 5),
        (4, 5),
    ]
    return edge_list, i_to_label


def get_triangle():
    i_to_label = HashMap()

    i_to_label[0] = '0'
    i_to_label[1] = '1'
    i_to_label[2] = '2'

    edge_list = [
        (0, 1),
        (1, 2),
        (2, 0)
    ]
    return edge_list, i_to_label


def test_coverters(edge_list):
    adj_mat = edge_list_to_adj_mat(edge_list)
    adj_list = adj_mat_to_adj_list(adj_mat)
    edge_list2 = adj_list_to_edge_list(adj_list)

    assert set(edge_list) == set(edge_list2), \
        f'\n{edge_list}\n{edge_list2}'

    print(f'Edge list:\n{edge_list}\n')
    print(f'Adj mat:\n{adj_mat}\n')
    print(f'Adj list:\n{adj_list}\n')


def main():
    print('=== triangle ===')
    edge_list, _ = get_triangle()
    test_coverters(edge_list)

    print('=== divisibility graph ===')
    edge_list, _ = get_divisibility_graph()
    test_coverters(edge_list)


if __name__ == '__main__':
    main()
