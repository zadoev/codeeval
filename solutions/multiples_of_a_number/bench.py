__author__ = 'zadoev@gmail.com'

import timeit

from main import solver

def solver2(x, n):
    """
    testing
    :param x:
    :type x:
    :param n:
    :type n:
    :return:
    :rtype:
    """
    if n > x:
        return n
    bx = bin(x)[2:]
    bn = bin(n)[2:]

    lbx = len(bx)
    lbn = len(bn)

    if lbx == lbn:
        return 1 << lbx

    res = x >> lbn
    res <<= lbn
    res |= n
    return res



print "solver: {}".format(
    timeit.timeit(lambda: solver(17,8), number=10000) +
    timeit.timeit(lambda: solver(7, 8), number=10000) +
    timeit.timeit(lambda: solver(117, 8), number=10000)
)

print "new solver: {}".format(
    timeit.timeit(lambda: solver2(17,8), number=10000) +
    timeit.timeit(lambda: solver2(7, 8), number=10000) +
    timeit.timeit(lambda: solver2(117, 8), number=10000)
)