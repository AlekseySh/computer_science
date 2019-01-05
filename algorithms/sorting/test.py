from random import randint


def test(sort_func,
         n_test=1000,
         size_bounds=(0, 10),
         val_bounds=(0, 10)
         ):
    for _ in range(n_test):
        x = [randint(*val_bounds) for _ in range(randint(*size_bounds))]

        x_for_default = x.copy()
        x_for_custom = x.copy()

        x_for_default.sort()  # default inplace sort
        sort_func(x_for_custom)  # custom inplace sort

        assert x_for_custom == x_for_default, \
            f'input: {x}, sorted: {x_for_custom}'

    print('Tests passed!')
