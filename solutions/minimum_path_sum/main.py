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


class Solver(object):
    """
    >>> s = Solver([[4, 6], [2, 8]])
    >>> s.solve()
    14
    >>> s = Solver([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> s.solve()
    21

    """
    def __init__(self, area):
        self.area = area
        self.size = len(area) - 1
        self.min_sum = None

    def solve(self, path_sum=0, x=0, y=0):
        if x == self.size and y == self.size:
            self.min_sum = min(
                filter(None, [self.min_sum, path_sum + self.area[x][y]])
            )

        if x + 1 <= self.size:
            self.solve(path_sum + self.area[x][y], x+1, y)

        if y + 1 <= self.size:
            self.solve(path_sum + self.area[x][y], x, y + 1)

        return self.min_sum


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            size = int(line.rstrip())
            area = []
            for i in xrange(size):
                area.append(map(int, next(test_cases).rstrip().split(',')))
            solver = Solver(area)
            print solver.solve()
