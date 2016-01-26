# -*- coding: utf-8 -*-
__author__ = 'zadoev@gmail.com'
"""
A robot is located in the upper-left corner of a 4×4 grid. The robot can move
either up, down, left, or right, but cannot go to the same location twice.
The robot is trying to reach the lower-right corner of the grid. Your task is
to find out the number of unique ways to reach the destination.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print out the number of unique ways for the robot to reach its destination.
The number should be printed out as an integer ≥0.
"""


def solver(area, pos, l):
    """
    >>> solver([[False, False], [False, False]], (0,0), 1)
    2
    >>> solver(
    ...    [
    ...        [False, False, False],
    ...        [False, False, False],
    ...        [False, False, False]
    ...    ],
    ...    (0,0),
    ...    2
    ... )
    12

    :param area:
    :type area:
    :param pos:
    :type pos:
    :param l:
    :type l:
    :return:
    :rtype:
    """
    x, y = pos

    if x == l and y == l:
        return 1

    if not (0 <= x <= l and 0 <= y <= l):
        return 0

    if area[x][y]:
        return 0

    area[x][y] = True

    result = 0

    result += solver(area, (x + 1, y), l)
    result += solver(area, (x - 1, y), l)
    result += solver(area, (x, y + 1), l)
    result += solver(area, (x, y - 1), l)

    area[x][y] = False

    return result

if __name__ == '__main__':
    print(solver(
        [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
        ],
        (0, 0)
        , 3
    ))
