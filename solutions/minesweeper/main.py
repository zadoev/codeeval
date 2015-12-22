__author__ = 'zadoev@gmail.com'

import sys


def solve(rows, columns, seq):
    """
    >>> list(solve(3, 5, '**.........*...'))
    ['*', '*', 1, 0, 0, 3, 3, 2, 0, 0, 1, '*', 1, 0, 0]

    :param rows:
    :type rows: int
    :param columns:
    :type columns: int
    :param seq: data for matrix
    :type seq: list
    :return:
    :rtype:
    """

    matrix = [i[:] for i in [[0] * (columns + 2)]*(rows+2)]
    for x in range(columns):
        for y in range(rows):
            if seq[y*columns + x] == '*':
                matrix[y+1][x+1] = 1
    for y in range(1, rows+1):
        for x in range(1, columns+1):
            if matrix[y][x]:
                yield '*'
            else:
                sum = 0
                for k in range(-1, 2):
                    for i in range(-1, 2):
                        sum += matrix[y+i][x+k]
                yield sum


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            size, seq = line.split(';')
            rows, columns = map(int, size.split(','))
            print ''.join(map(str, solve(rows, columns, seq.rstrip())))
