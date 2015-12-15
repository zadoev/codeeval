__author__ = 'zadoev@gmail.com'
"""
Imagine we have an immutable array of size N which we know to be filled with
integers ranging from 0 to N-2, inclusive. Suppose we know that the array
contains exactly one duplicated entry and that duplicate appears exactly twice.
Find the duplicated entry. (For bonus points, ensure your solution has
constant space and time proportional to N)

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each
line in this file is one test case. Ignore all empty lines. Each line begins
with a positive integer(N) i.e. the size of the array, then a semicolon followed
by a comma separated list of positive numbers ranging from 0 to N-2, inclusive.
i.e eg.

5;0,1,2,3,0
20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14
OUTPUT SAMPLE:

Print out the duplicated entry, each one on a new line eg

0
4
"""

import sys
from itertools import imap


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
    :type n: int
    :param seq: elements
    :type seq: list
    :return: duplicated number
    :rtype: int
    """

    return sum(seq) - (n-1) * (n-2) / 2


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            n, seq = line.rstrip().split(';')
            seq = seq.split(',')

            print solve(int(n), imap(int, seq))
