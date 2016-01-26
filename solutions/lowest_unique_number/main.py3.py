__author__ = 'zadoev@gmail.com'
"""
There is a game where each player picks a number from 1 to 9, writes it on a
paper and gives to a guide. A player wins if his number is the lowest unique.
We may have 10-20 players in our game.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.

You're a guide and you're given a set of numbers from players for the round of
game. E.g. 2 rounds of the game look this way:

3 3 9 1 6 5 8 1 5 3
9 2 9 9 1 8 8 8 2 1 1
OUTPUT SAMPLE:

Print a winner's position or 0 in case there is no winner. In the first line
of input sample the lowest unique number is 6. So player 5 wins.

5
0
"""
import sys

from collections import Counter


def solve(seq):
    """
    >>> solve([1,2])
    1
    >>> solve([1,1])
    0
    >>> solve([3, 3, 9, 1, 6, 5, 8, 1, 5, 3])
    5
    >>> solve([9, 2, 9, 9, 1, 8, 8, 8, 2, 1, 1])
    0

    :param seq:
    :type seq:
    :return:
    :rtype:
    """
    seq = list(seq)
    c = Counter(seq)
    unique_numbers = [i for i, k in c.items() if k == 1]
    if not unique_numbers:
        return 0
    return seq.index(min(unique_numbers)) + 1


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print(solve(map(int, line.split())))
