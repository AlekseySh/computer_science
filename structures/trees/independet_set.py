from functools import lru_cache

from structures.trees.tree import get_sample_tree


def find_size_of_max_independent_set(root_node):
    @lru_cache(1000)
    def step(cur_node):
        global size

        if cur_node.has_no_child():
            return 1

        else:
            a = sum([step(node) for node in cur_node.get_children()])
            b = sum([step(node) for node in cur_node.get_grandchildren()]) + 1
            return max(a, b)

    size = step(root_node)
    return size


def main():
    tree_root, ind_size_gt = get_sample_tree()
    ind_size = find_size_of_max_independent_set(tree_root)

    assert ind_size == ind_size_gt, \
        f'Answer is incorrect, gt: {ind_size_gt}, pred: {ind_size}.'


if __name__ == '__main__':
    main()
