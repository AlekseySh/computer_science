import numpy as np


def pack_bug(weights, prices, max_w):
    n_obj = len(weights)

    # 1. ind answer

    a = - np.ones((n_obj + 1, max_w + 1), np.int)
    a[0, :] = a[:, 0] = 0

    for k in range(1, n_obj + 1):

        for s in range(1, max_w + 1):

            if s >= weights[k - 1]:
                # put this object
                a[k, s] = max(a[k - 1, s],
                              a[k - 1, s - weights[k - 1]] + prices[k - 1]
                              )
            else:
                # don't put this object
                a[k, s] = a[k - 1, s]

    print(a)

    # 2. restore indeces

    def find(k_, s_):
        if a[k_, s_] == 0:
            return

        if a[k_ - 1, s_] == a[k_, s_]:
            find(k_ - 1, s_)

        else:
            find(k_ - 1, s_ - weights[k_ - 1])
            ii_pick.append(k_ - 1)

    ii_pick = []
    k_init, s_init = n_obj, max_w

    find(k_init, s_init)

    return ii_pick


def get_sample():
    weights = [3, 4, 5, 8, 9, 1, 1]
    prices = [1, 6, 4, 7, 6, 1, 1]
    max_w = 14  # max weight

    ii_pick_gt = [1, 3, 5, 6]

    return weights, prices, max_w, ii_pick_gt


def test(sample):
    weights, prices, max_w, ii_pick_gt = sample

    ii_pick = pack_bug(weights=weights,
                       prices=prices,
                       max_w=max_w)

    picked_weight_gt = sum([weights[i] for i in ii_pick_gt])
    picked_weight = sum([weights[i] for i in ii_pick])

    picked_price_gt = sum([prices[i] for i in ii_pick_gt])
    picked_price = sum([prices[i] for i in ii_pick])

    print(f'FOUND: price: {picked_price}, weight: {picked_weight}')
    print(f'GT: price: {picked_price_gt}, weight: {picked_weight_gt}')

    assert (picked_weight_gt == picked_weight) and \
           (picked_price_gt == picked_price), \
        'Answer is incorrect'

    print('Test passed.')


def main():
    test(sample=get_sample())


if __name__ == '__main__':
    main()
