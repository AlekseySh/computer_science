import numpy as np

from algorithms.hashing import hash_func
from structures.list import List

__all__ = ['HashMap']


class KeyVal:

    def __init__(self, key, val):
        self.key, self.val = key, val

    def key(self): return self.key

    def val(self): return self.val

    def __str__(self):
        return f'<{self.key}: {self.val}>'


class HashMap:
    table_size = 101  # better use simple number

    def __init__(self):
        self.len = 0
        self.keys = List()

        self.h = np.repeat(None, self.table_size)
        self.hash_f = lambda x: hash_func(x, self.table_size)

    def __str__(self):
        text = '{ \n'
        for key in self.keys:

            if isinstance(key, str):
                key_str = f'\'{key}\''
            else:
                str(key)

            text += f'{key_str}: {str(self[key])}\n'
        text += '}'
        return text

    def __setitem__(self, key, val):
        idx = self.hash_f(key)

        if key in self.keys:
            add_idx = HashMap._find_key_in_list(self.h[idx], key)
            self.h[idx][add_idx].val = val
        else:
            if not self.h[idx]:
                self.h[idx] = List()

            self.h[idx].append(KeyVal(key, val))

            self.keys.append(key)
            self.len += 1

    def __delitem__(self, key):
        idx = self.hash_f(key)
        add_idx = HashMap._find_key_in_list(self.h[idx], key)
        self.len -= 1

        del self.h[idx][add_idx]
        del self.keys[self.keys.find(key)]

    def __getitem__(self, key):
        idx = self.hash_f(key)
        add_idx = HashMap._find_key_in_list(self.h[idx], key)
        val = self.h[idx][add_idx].val
        return val

    def __len__(self):
        return self.len

    def print_structure(self):
        print('Hash-map inner structure:')
        for i, kv_list in enumerate(self.h):
            print(f'h_{i}| {kv_list}')

    @staticmethod
    def _find_key_in_list(kv_list, key):
        # assume that kv_list contains KeyVal objs
        for idx, kv in enumerate(kv_list):
            if kv.key == key:
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
    hash_map[124] = 7

    hash_map['4'] = 0

    del hash_map['0']

    hash_map.print_structure()
    print(hash_map)
