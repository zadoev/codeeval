__author__ = 'zadoev@gmail.com'
"""
You are given a sorted array of positive integers and a number 'X'.
Print out all pairs of numbers whose sum is equal to X. Print out only
unique pairs and the pairs should be in ascending order

INPUT SAMPLE:

Your program should accept as its first argument a filename. This file will
contain a comma separated list of sorted numbers and then the sum 'X', separated
by semicolon. Ignore all empty lines. If no pair exists, print the string NULL
e.g.

1,2,3,4,6;5
2,4,5,6,9,11,15;20
1,2,3,4;50
OUTPUT SAMPLE:

Print out the pairs of numbers that equal to the sum X. The pairs should
themselves be printed in sorted order i.e the first number of each pair
should be in ascending order. E.g.

1,4;2,3
5,15;9,11
NULL
"""

import sys
from itertools import imap, ifilter
import string


def solve(seq, expected):
    """
    >>> list(solve([1,5], 6))
    [(1, 5)]

    >>> list(solve([1,3], 6))
    []

    >>> list(solve([1,2,3,4,6], 5))
    [(1, 4), (2, 3)]

    >>> list(solve([2,4,5,6,9,11,15], 20))
    [(5, 15), (9, 11)]

    >>> list(solve([100, 101, 102], 20))
    []

    :param seq: sorted number sequence
    :type seq: list
    :param expected: number to find pairs with sum equal
    :type expected: int
    :return: sequence of pairs
    :rtype: basestring
    """
    i = 0
    j = len(seq) - 1

    while i < j:
        a = seq[i]
        b = seq[j]
        if a > expected:
            break

        current_sum = a + b
        if current_sum == expected:
            yield '{},{}'.format(a, b)
            i += 1
            continue
        if current_sum > expected:
            j -= 1
        else:
            i += 1


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in ifilter(len, imap(string.rstrip, test_cases)):
            seq, expected = line.split(';')
            res = list(solve(map(int, seq.split(',')), int(expected)))
            if not res:
                res = ['NULL']

            print ';'.join(res)
