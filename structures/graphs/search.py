import warnings

import networkx as nx
from matplotlib import pyplot as plt

import structures.graphs.graphs as g
from structures.list import List
from structures.queue import Queue
from structures.stack import Stack


def dfs(adj_list, ii_start):
    visited, ii_order = set(), List()

    def step(idx):
        if idx in visited:
            return

        else:
            visited.add(idx)
            ii_order.append(idx)

            for j in adj_list[idx]:
                step(j)

    for node_idx in ii_start:
        step(node_idx)

    return ii_order


def top_sort(adj_list):
    n = len(adj_list)
    colors = ['w'] * n
    stack = Stack()

    def dfs_step(idx):
        if colors[idx] == 'g':
            raise ValueError('Cycle was find.')

        if colors[idx] == 'w':
            colors[idx] = 'g'

            for j in adj_list[idx]:
                dfs_step(j)

            colors[idx] = 'b'
            stack.push(idx)

    for i0 in range(n):
        dfs_step(i0)

    ii_order = stack.to_list()
    return ii_order


def bfs(adj_list, i_start=0):
    visited, ii_order = set(), List()
    queue = Queue()

    queue.enqueue(i_start)
    visited.add(i_start)
    ii_order.append(i_start)

    def step():
        if not queue:
            return
        else:
            i = queue.dequeue()
            for j in adj_list[i]:
                if j not in visited:
                    visited.add(j)
                    ii_order.append(j)
                    queue.enqueue(j)
            step()

    step()
    return ii_order


def search_check(graph):
    edge_list, i_to_labels = graph
    adj_list = g.edge_list_to_adj_list(edge_list)

    i_start = 0

    bfs_ii = bfs(adj_list, i_start=i_start)
    bfs_labels = [i_to_labels[i] for i in bfs_ii]
    print(f'BFS from [{i_start}]:\n {bfs_labels}\n')

    dfs_ii = dfs(adj_list, ii_start=[i_start])
    dfs_labels = [i_to_labels[i] for i in dfs_ii]
    print(f'DFS from [{i_start}]:\n {dfs_labels}\n')

    assert set(dfs_ii) == set(bfs_ii), \
        'Sets of reachable nodes must be the same.'


def top_sort_check(graph):
    edge_list, i_to_labels = graph
    adj_list = g.edge_list_to_adj_list(edge_list)

    # draw(edge_list, i_to_labels)

    # our
    ii_sort = top_sort(adj_list)
    labels_sort = [i_to_labels[i] for i in ii_sort]

    # lib
    dig = nx.DiGraph()
    dig.add_edges_from(edge_list)
    ii_sort_lib = list(nx.topological_sort(dig))
    labels_sort_lib = [i_to_labels[i] for i in ii_sort_lib]

    print(f'Topological sort: {labels_sort_lib} (lib).')
    print(f'Topological sort: {labels_sort} (our).')


def draw(edge_list, labels):
    warnings.filterwarnings("ignore")

    labels_str = {key: f'\'{val}\' [{key}]' for key, val in labels.items()}

    g = nx.DiGraph()
    g.add_edges_from(edge_list)
    pos = nx.spring_layout(g)

    plt.figure()
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(
        g, pos, labels=labels_str, font_size=16)
    plt.axis('off')
    plt.show()


def main():
    graph = g.get_divisibility_graph()
    search_check(graph)
    top_sort_check(graph)


if __name__ == '__main__':
    main()
