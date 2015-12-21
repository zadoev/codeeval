__author__ = 'zadoev@gmail.com'
"""
CHALLENGE DESCRIPTION:

You are given an n*n matrix of integers. You can move only right and down.
Calculate the minimal path sum from the top left to the bottom right

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.
The first line will have the value of n(the size of the square matrix).
This will be followed by n rows of the matrix. (Integers in these rows will
be comma delimited). After the n rows, the pattern repeats. E.g.

2
4,6
2,8
3
1,2,3
4,5,6
7,8,9
OUTPUT SAMPLE:

Print out the minimum path sum for each matrix. E.g.

14
21
"""
import sys


def solve(matrix, size):
    """
    >>> solve([[4, 6], [2, 8]], 2)
    14

    >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)
    21

    :param matrix: input matrix
    :type matrix: list of lists
    :param size: matrix size
    :type size: int
    :return: minimum path sum for matrix
    :rtype: int
    """
    if size == 1:
        return matrix[0][0]

    for x in xrange(size-2, -1, -1):
        # calculate min paths for right, bottom borders
        matrix[size-1][x] += matrix[size-1][x+1]
        matrix[x][size-1] += matrix[x+1][size-1]

    for y in xrange(size - 2, -1, -1):
        for x in xrange(size-2, -1, -1):
            # calculate min path from right and bottom
            # doing from right to left, from bottom to up
            # excluding pre calculated borders
            matrix[x][y] += min(matrix[x+1][y], matrix[x][y+1])

    return matrix[0][0]

if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            size = int(line.rstrip())
            area = []
            for i in xrange(size):
                area.append(map(int, next(test_cases).rstrip().split(',')))
            print solve(area, size)
