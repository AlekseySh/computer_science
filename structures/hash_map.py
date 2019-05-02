import numpy as np

from algorithms.hashing import hash_func
from structures.list import List

__all__ = ['HashMap']


class KeyVal:

    def __init__(self, key, val):
        self.key, self.val = key, val

    def __str__(self):
        return f'<{self.key}: {self.val}>'


class HashMap:
    table_size = 15  # better use a prime number

    def __init__(self):
        self.len = 0
        self.arr = np.repeat(None, self.table_size)

    def __setitem__(self, key, val):
        idx = self.hash_func(key)
        kv_list = self.arr[idx]

        if kv_list is None:
            self.arr[idx] = List()
            self.arr[idx].append(KeyVal(key=key, val=val))
            self.len += 1
        else:
            kv_idx = HashMap._find_key_in_list(kv_list, key)
            if kv_idx is None:
                self.arr[idx].append(KeyVal(key=key, val=val))
                self.len += 1
            else:
                self.arr[idx][kv_idx].val = val

    def __getitem__(self, key):
        kv_list = self.arr[self.hash_func(key)]
        if kv_list is None:
            raise ValueError(f'Unexpected key {key}')

        kv_idx = HashMap._find_key_in_list(kv_list, key)
        if kv_idx is None:
            raise ValueError(f'Unexpected key {key}')
        else:
            return kv_list[kv_idx].val

    def __delitem__(self, key):
        kv_list = self.arr[self.hash_func(key)]
        if kv_list is None:
            raise ValueError(f'Unexpected key {key}')

        kv_idx = HashMap._find_key_in_list(kv_list, key)
        if kv_idx is None:
            raise ValueError(f'Unexpected key {key}')
        else:
            del kv_list[kv_idx]
            self.len -= 1

    def __len__(self):
        return self.len

    def __str__(self):
        text = '{'
        for kv_list in self.arr:
            if kv_list is not None:
                text += f'{self._kv_list_to_str(kv_list)}'
        text += '}'
        return text

    def hash_func(self, x):
        return hash_func(x, self.table_size)

    def print_structure(self):
        print('\nHash-map inner structure:')
        for i, kv_list in enumerate(self.arr):
            if kv_list is not None:
                kv_list_str = self._kv_list_to_str(kv_list)
                print(f'cell {i}| {kv_list_str}')
            else:
                print(f'cell {i} | - ')

    @staticmethod
    def _kv_list_to_str(kv_list):
        def str_repr(x):
            return f'\'{x}\'' if isinstance(x, str) else str(x)

        text = ''
        for kv in kv_list:
            text += f'{str_repr(kv.key)}: {str_repr(kv.val)}, '
        return text

    @staticmethod
    def _find_key_in_list(kv_list, key):
        # assume that kv_list contains KeyVal objs
        idx = None
        for i, kv in enumerate(kv_list):
            if kv.key == key:
                idx = i
        return idx


if __name__ == '__main__':
    hash_map = HashMap()

    hash_map['1'] = 1
    hash_map['2'] = 2
    hash_map['3'] = 3
    hash_map['4'] = 4
    hash_map['5'] = '5'
    hash_map[124] = '7'

    hash_map['4'] = 0

    print(hash_map['2'])
    print(hash_map[124])

    hash_map.print_structure()
    del hash_map['2']

    hash_map.print_structure()
    print(hash_map)
