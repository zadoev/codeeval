from __future__ import print_function
__author__ = 'zadoev@gmail.com'
import itertools
import sys

ANSWERS = ('Not jolly', 'Jolly')


def solve(seq):
    """
    >>> solve(itertools.imap(int, [4, 1, 4, 2, 3]))
    True

    >>> solve(itertools.imap(int, (4, 3, 7, 7, 8)))
    False

    >>> solve(itertools.imap(int, (10, 9, 8, 9, 7, 10, 6, 12, 17, 24, 38)))
    False

    >>> solve(itertools.imap(int, (10, 1, 2, 3, 4)))
    False

    >>> solve(itertools.imap(int, (5, 1, 5, 2, 4, 3)))
    True

    >>> solve(itertools.imap(int, [1, 1]))
    True

    >>> solve(itertools.imap(int, [2, 1, 2]))
    True

    >>> solve(itertools.imap(int, [4, 2, 1, 2, 1]))
    False

    :param seq: sequence to detect if jolly
    :rtype: True if jolly jumpers otherwise False
    """

    n = next(seq)
    it, copy = itertools.tee(seq)

    next(copy)
    diffs = set(abs(x -y) for x, y in itertools.izip(it, copy))
    return diffs == set(xrange(1, n))


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print(ANSWERS[solve(itertools.imap(int, line.split()))])
