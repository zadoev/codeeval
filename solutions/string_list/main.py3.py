__author__ = 'zadoev@gmail.com'
"""
CHALLENGE DESCRIPTION:

Credits: Challenge contributed by Max Demian.

You are given a number N and a string S. Print all of the possible ways to write
a string of length N from the characters in string S, comma delimited in
alphabetical order.

INPUT SAMPLE:

The first argument will be the path to the input filename containing the test
data. Each line in this file is a separate test case. Each line is in the
format: N,S i.e. a positive integer, followed by a string (comma separated).
E.g.

1,aa
2,ab
3,pop
OUTPUT SAMPLE:

Print all of the possible ways to write a string of length N from the characters
in string S comma delimited in alphabetical order, with no duplicates. E.g.
"""

from itertools import product
import sys


def solve(n, seq):
    """
    >>> solve(1, 'aa')
    'a'
    >>> solve(2, 'ab')
    'aa,ab,ba,bb'
    >>> solve(3, 'pop')
    'ooo,oop,opo,opp,poo,pop,ppo,ppp'

    :param n:
    :type n:
    :param seq:
    :type seq:
    :return:
    :rtype:
    """
    return ','.join(
        list(
            map(
                lambda x: ''.join(x),
                product(
                    sorted(set(seq)),
                    repeat=n
                )
            )
        )
    )


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            num, instr = line.split(',')
            print(solve(int(num), instr.rstrip()))
