__author__ = 'zadoev@gmail.com'
"""
DISTINCT SUBSEQUENCES
CHALLENGE DESCRIPTION:

A subsequence of a given sequence S consists of S with zero or more elements
deleted. Formally, a sequence Z = z1z2..zk is a subsequence of X = x1x2...xm,
if there exists a strictly increasing sequence of indicies of X such that for
all j=1,2,...k we have Xij = Zj. E.g. Z=bcdb is a subsequence of X=abcbdab with
corresponding index sequence <2,3,5,7>

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.
Each line in this file contains two comma separated strings. The first is the
sequence X and the second is the subsequence Z. E.g.

babgbag,bag
rabbbit,rabbit
OUTPUT SAMPLE:

Print out the number of distinct occurrences of Z in X as a subsequence E.g.

5
3

Used: http://www.cs.cmu.edu/~yandongl/distinctseq.html

"""

import sys


def solve(s1, s2):
    """
    >>> solve('aabb','ab')
    4
    >>> solve('abc', 'ac')
    1
    >>> solve('babgbag', 'bag')
    5
    >>> solve('rabbbit', 'rabbit')
    3

    """

    s2len = len(s2)

    computer = [0]*(s2len+1)
    computer[0] = 1

    for i in range(0, len(s1)):
        last = computer[0]
        for j in range(0, s2len):
            this = computer[j+1]
            if s1[i] == s2[j]:
                computer[j+1] += last
            last = this
    return computer.pop()


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            s1, s2 = line.split(',')
            print solve(s1, s2.rstrip())
