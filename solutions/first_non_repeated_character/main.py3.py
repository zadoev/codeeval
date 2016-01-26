"""
Write a program which finds the first non-repeated character in a string.

INPUT SAMPLE:

The first argument is a path to a file. The file contains strings.

For example:

yellow
tooth
OUTPUT SAMPLE:

Print to stdout the first non-repeated character, one per line.

For example:

y
h

"""

import sys

from collections import Counter

def solve(seq):
    """
    Finds in given sequence first non repeated character

    >>> solve('abc')
    'a'
    >>> solve('ababcd')
    'c'
    >>> solve('yellow')
    'y'
    >>> solve('tooth')
    'h'

    :param seq: string to find first non repeated character (can be iterable)
    :type seq: basestring
    :return:
    :rtype: basestring
    """
    c = Counter(seq)
    return next(filter(lambda i: c.get(i) == 1, seq))


if __name__ == '__main__':
    with open(sys.argv[1]) as test_case:
        for line in test_case:
            print(solve(line.rstrip()))
