"""
__author__ = 'zadoev@gmail.com'
https://www.codeeval.com/open_challenges/43/
"""

import sys
import itertools


ANSWERS = ('Not jolly', 'Jolly')


def solve(n, seq):
    """
    >>> solve(4, [1, 4, 2, 3])
    True

    >>> solve(5, (4, 3, 7, 7, 8))
    False

    >>> solve(10, (9, 8, 9, 7, 10, 6, 12, 17, 24, 38))
    False

    >>> solve(10, (1, 2, 3, 4))
    False

    >>> solve(5, (1, 5, 2, 4, 3))
    True

    >>> solve(1, [1])
    True

    >>> solve(2, [1, 2])
    True

    >>> solve(4, [2, 1, 2, 1])
    False

    :param seq: sequence to detect if jolly
    :rtype: True if jolly jumpers otherwise False
    """

    it, copy = itertools.tee(seq)

    next(copy)
    diffs = set(abs(x -y) for x, y in zip(it, copy))
    return diffs == set(range(1, n))


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            int_gen = map(int, line.split())
            print(ANSWERS[solve(next(int_gen), int_gen)])
