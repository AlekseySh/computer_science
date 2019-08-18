import warnings

import networkx as nx
from matplotlib import pyplot as plt

import structures.graphs.graphs as g
from structures.list import List
from structures.queue import Queue
from structures.stack import Stack


# Algos

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


def dfs_colored_step(idx, adj_list, colors, stack):
    if colors[idx] == 'g':
        is_cycle = True
        return is_cycle

    if colors[idx] == 'w':
        colors[idx] = 'g'

        for j in adj_list[idx]:
            dfs_colored_step(j, adj_list, colors, stack)

        colors[idx] = 'b'

        if stack is not None:
            stack.push(idx)

        is_cycle = False
        return is_cycle


def top_sort(adj_list):
    n = len(adj_list)
    colors = ['w'] * n
    stack = Stack()

    for i0 in range(n):
        is_cycle = dfs_colored_step(i0, adj_list, colors, stack)

        if is_cycle:
            raise ValueError('Cycle was found')

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


def find_source_and_stock(edge_list):
    # only for orient graphs
    edges = {idx for edge in edge_list for idx in edge}
    n_v = len(edges)

    inp, out = [0] * n_v, [0] * n_v

    for u, v in edge_list:
        inp[v] += 1
        out[u] += 1

    ii_source = [i for i in range(n_v) if inp[i] == 0]
    ii_stock = [i for i in range(n_v) if out[i] == 0]

    return ii_source, ii_stock


def find_linked_components(adj_list):
    # only for nonor graphs
    n = len(adj_list)
    colors = ['w'] * n
    components = []

    for i0 in range(n):

        stack = Stack()
        dfs_colored_step(i0, adj_list, colors, stack)
        component = set(stack.to_list())

        if component:
            components.append(component)

    return components


# Tests

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


def source_and_stock_check(edge_list, ii_source_gt, ii_stock_gt):
    ii_source, ii_stock = find_source_and_stock(edge_list)

    assert set(ii_source_gt) == set(ii_source)
    assert set(ii_stock_gt) == set(ii_stock)


def top_sort_check(graph):
    edge_list, i_to_labels = graph
    adj_list = g.edge_list_to_adj_list(edge_list)

    draw(edge_list, i_to_labels)

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


def components_check():
    edge_list, _ = g.get_two_triangles_graph()
    first_comp_gt = {0, 1, 2}
    second_comp_gt = {3, 4, 5}

    adj_list = g.edge_list_to_adj_list(edge_list)
    components = find_linked_components(adj_list)

    print(components)

    assert len(components) == 2
    assert (first_comp_gt in components) and \
           (second_comp_gt in components)


def test_or_graphs():
    print('\nTest on orient graphs.')

    search_check(g.get_divisibility_graph())
    search_check(g.get_triangle())

    top_sort_check(g.get_divisibility_graph())

    source_and_stock_check(g.get_divisibility_graph()[0],
                           [1], [5])

    print('All checks are passed.')


def test_nonor_graphs():
    print('\nTest on non-orient graphs.')

    search_check(g.get_divisibility_nonor_graph())
    search_check(g.get_triangle_nonor())

    components_check()

    print('All checks are passed.')


# Visualization

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
    test_or_graphs()
    test_nonor_graphs()


if __name__ == '__main__':
    main()
