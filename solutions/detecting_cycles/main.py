__author__ = 'zadoev@gmail.com'

import sys


def floyd(seq):
    """
    Fload algo

    >>> floyd([1, 2, 3, 1, 2, 3])
    [1, 2, 3]

    >>> floyd(map(int,'2 0 6 3 1 6 3 1 6 3 1'.split()))
    [6, 3, 1]

    >>> floyd(map(int,'3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49'.split()))
    [49]

    :param seq: list of nums
    :type seq: list
    :return: list with cycle
    :rtype: list
    """
    x, y = 0, 1
    seq_len = len(seq)
    while seq[x] != seq[y]:
        x = (x + 1) % seq_len
        y = (y + 2) % seq_len

    begin = 0
    y, x = abs(y - x), 0
    while seq[x] != seq[y]:
        x = (x + 1) % seq_len
        y = (y + 1) % seq_len
        begin += 1

    length, y = 1, x + 1
    while seq[x] != seq[y]:
        y += 1
        length += 1

    return seq[begin: begin + length]


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print ' '.join(map(str, floyd(map(int, line.split()))))
