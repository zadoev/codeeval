__author__ = 'zadoev@gmail.com'
"""
You have a N story building and K eggs. They are especially strong eggs so
they're able to withstand impact up to a certain number of floors.

Your goal is to identify the number of drops you need make to determine number
of floors it can withstand.

INPUT SAMPLE:

The first argument will be a path to a filename containing a space separated
list of 2 integers, first one is number eggs, second one - number of floors.
E.g.

2 100
OUTPUT SAMPLE:

The output contains one integer - the worst worst case upper bound on the
number of drops you must make to determine this floor.

14

"""
import sys
import math
from ctypes import c_uint


def solver(k, n):
    """
    >>> #solver(1,1) # [[0, 0], [0, 1]] test init, now not need
    >>> #solver(2,2) # [[0, 0, 0], [0, 1, 1], [0, 2, 1]] test init, now not need
    >>> solver(2, 5)
    3L
    >>> solver(2, 6)
    3L
    >>> solver(2, 100)
    14L
    >>> solver(10, 1000)
    10

    :param n: floors
    :type n: int
    :param k: eggs
    :type k: int
    :return: minimum drops for worst keys
    :rtype: int
    """

    ln = int(math.ceil((math.log(n, 2))))
    if k >= ln:
        return ln

    KInts = c_uint * (k+1)
    Mtrx = KInts * (n + 1)
    matrix = Mtrx()

    for floor in xrange(1, n + 1):
        matrix[floor][1] = floor

    for egg in xrange(k+1):
        matrix[1][egg] = 1

    for floor in xrange(2, n+1):
        ln = 1 + int(math.log(n, 2))
        egg_range = k + 1
        if k + 1 > ln:
            egg_range = ln
            for egg in xrange(ln, k+1):
                matrix[floor][egg] = ln

        for egg in xrange(2, egg_range):
            i = 1
            j = floor + 1
            m = j / 2
            min_of_max = None
            while min_of_max is None:
                av, bv = matrix[m - 1][egg - 1], matrix[floor - m][egg]
                if av == bv:
                    min_of_max = av + 1
                    break

                if av > bv:
                    j = m
                    r = av + 1
                else:
                    i = m
                    r = bv + 1
                m = (j + i) / 2

                if i + 1 == j:
                    min_of_max = r

            matrix[floor][egg] = min_of_max

    return matrix[n][k]


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print solver(*map(int, line.split(' ')))

