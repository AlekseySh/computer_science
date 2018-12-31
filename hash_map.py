import numpy as np

from list import List


class HashMap:
    table_size = 10

    def __init__(self):
        self.len = 0
        self.keys = set()
        self.h = np.repeat(None, self.table_size)
        self.hash_f = lambda x: hash(x) % self.table_size

    def __str__(self):
        text = '{ \n'
        for key in self.keys:
            key_str = f'\'{key}\'' if isinstance(key, str) else str(key)
            text += f'{key_str}: {str(self[key])}\n'
        text += '}'
        return text

    def __setitem__(self, key, val):
        idx = self.hash_f(key)

        if key in self.keys:
            add_idx = HashMap._find_key_in_list(self.h[idx], key)
            self.h[idx][add_idx].val[1] = val
        else:
            if not self.h[idx]:
                self.h[idx] = List()

            key_val_list = List()
            key_val_list.append(key)
            key_val_list.append(val)
            self.h[idx].append(key_val_list)

            self.keys.add(key)
            self.len += 1

    def __delitem__(self, key):
        idx = self.hash_f(key)
        add_idx = HashMap._find_key_in_list(self.h[idx], key)
        self.h[idx].remove(add_idx)
        self.keys.remove(key)
        self.len -= 1

    def __getitem__(self, key):
        idx = self.hash_f(key)
        add_idx = HashMap._find_key_in_list(self.h[idx], key)
        node = self.h[idx][add_idx]
        return node.val[1]

    def __len__(self):
        return self.len

    def print_structure(self):
        print()
        for i, key_val_list in enumerate(self.h):
            print(f'{i}| {key_val_list}')

    @staticmethod
    def _find_key_in_list(key_val_list, key):
        # assume that list contains pairs (key, val)
        for idx, node in enumerate(key_val_list):
            if node.val[0].val == key:
                return idx
        raise ValueError


if __name__ == '__main__':
    hash_map = HashMap()

    hash_map['0'] = 0
    hash_map['1'] = 1
    hash_map['2'] = 2
    hash_map['3'] = 3
    hash_map['4'] = 4
    hash_map['5'] = 5

    hash_map['4'] = 0

    del hash_map['1']

    hash_map.print_structure()

    print()
    print(hash_map)
