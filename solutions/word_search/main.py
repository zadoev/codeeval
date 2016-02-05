__author__ = 'zadoev@gmail.com'
"""
https://www.codeeval.com/open_challenges/65/
"""

import sys
from collections import defaultdict

COL_CNT = 4
ROW_CNT = 3

MATRIX = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E'],
]

# a little overhead for memory, but matrix not huge, avoid calculation in
# recursion
POSSIBLE_WAYS = defaultdict(list)
CHAR_POINTS = defaultdict(list)
for r in range(0, ROW_CNT):
    for c in range(0, COL_CNT):
        CHAR_POINTS[MATRIX[r][c]].append((r, c))
        if r-1 >= 0:
            POSSIBLE_WAYS[(r, c)].append((r-1, c))
        if r+1 < ROW_CNT:
            POSSIBLE_WAYS[(r, c)].append((r+1, c))

        if c-1 >= 0:
            POSSIBLE_WAYS[(r, c)].append((r, c-1))
        if c+1 < COL_CNT:
            POSSIBLE_WAYS[(r, c)].append((r, c+1))

# helpers to cut off evident wrong cases
SIZE = ROW_CNT * COL_CNT


def find(seq, visited, point):
    """
    wave algo to find

    >>> find(list('ASADB'), [], (0, 0))
    False
    >>> find(list('ABCCED'), [], (0, 0))
    True
    >>> find(['A', 'B'], [], (0, 0))
    True
    >>> find(['A', 'D', 'F'], [], (2, 0))
    True
    >>> find(list('ASADFBCCEESE'), [], (0, 0))
    True
    """
    if point in visited:
        return False

    current_char = seq[0]

    if MATRIX[point[0]][point[1]] != current_char:
        return False

    if len(seq) == 1:
        return True

    visited.append(point)

    for new_point in POSSIBLE_WAYS[point]:
        if find(seq[1:], visited, new_point):
            return True

    visited.pop()
    return False


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            word = list(line.rstrip())
            r = False
            if len(word) <= SIZE:
                for point in CHAR_POINTS[word[0]]:
                    if find(word, [], point):
                        r = True
                        break
            print r
