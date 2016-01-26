"""
https://www.codeeval.com/open_challenges/41
"""

import sys


def solve(n, seq):
    """
    we have arithmetic progression from 0 to n-2 with step 1 with one extra
    value from duplicate, so last element is n-2 and we have n-1 items in
    progression

    >>> solve(5, [0,1,2,3,0])
    0
    >>> solve(20, [0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14])
    4

    :param n: range of elements
    :param seq: elements
    :return: duplicated number
    :rtype: int
    """

    return sum(seq) - (n-1) * (n-2) / 2


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            n, seq = line.rstrip().split(';')
            seq = seq.split(',')

            print(int(solve(int(n), map(int, seq))))
