"""
CHALLENGE DESCRIPTION:

Write a program to print a 2D array (n x m) in spiral order (clockwise)

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.
The input file contains several lines. Each line is one test case. Each line
contains three items (semicolon delimited). The first is 'n'(rows), the second
is 'm'(columns) and the third is a single space separated list of
characters/numbers in row major order. E.g.

3;3;1 2 3 4 5 6 7 8 9
OUTPUT SAMPLE:

Print out the matrix in clockwise fashion, one per line, space delimited. E.g.

1 2 3 6 9 8 7 4 5
"""

import sys


def solver(rows, columns, input_items):
    """
    >>> list(solver(3,3, ['1','2','3','4','5','6','7','8','9']))
    ['1 2 3', '6 9', '8 7', '4', '5']

    :param rows: number of rows in array
    :type rows: int
    :param columns: number of columns
    :type columns: int
    :param input_items: input data
    :type input_items: list
    :return: generator for strings
    :rtype: list[strings]
    """
    data = []
    for i in range(rows):
        data.append(input_items[i*columns:(i+1)*columns])
    while data:
        row = data.pop(0)
        data = list(zip(*data))
        data.reverse()
        yield ' '.join(row)


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            n, m, items = line.split(';')
            n, m = int(n), int(m)
            for part in solver(n, m, items.split()):
                print (part, end=' ')
            print()
