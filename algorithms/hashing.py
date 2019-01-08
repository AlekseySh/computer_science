"""
Based on:
https://en.wikipedia.org/wiki/Universal_hashing
"""

__all__ = ['hash_func']


def hash_func(val, hash_size=101):
    if isinstance(val, str):
        hash_val = hash_str(val, hash_size)

    elif isinstance(val, int):
        hash_val = hash_int(val, hash_size)

    else:
        raise TypeError(f'Unexpected input type: {type(val)}')

    return hash_val


def hash_str(string, hash_size):
    s = 0
    for c in string:
        s += hash_char(c, hash_size)
    hash_val = s % hash_size
    return hash_val


def hash_int(number, hash_size):
    hash_val = number % hash_size
    return hash_val


def hash_char(character, hash_size):
    hash_val = hash_int(ord(character), hash_size)
    return hash_val


if __name__ == '__main__':

    values = [1231, -13, '11vwe', '23vv21', 'e']
    for v in values:
        print(f'value: {v}, hash: {hash_func(v, 101)}')
