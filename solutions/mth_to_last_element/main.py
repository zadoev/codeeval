__author__ = 'zadoev@gmail.com'
"""
Write a program which determines the Mth to the last element in a list.

INPUT SAMPLE:

The first argument is a path to a file. The file contains the series of space
delimited characters followed by an integer. The integer represents an index
in the list (1-based), one per line.

For example:

a b c d 4
e f g h 2
OUTPUT SAMPLE:

Print to stdout the Mth element from the end of the list, one per line. If the
index is larger than the number of elements in the list, ignore that input.

For example:

a
g
"""

import sys


def solver(seq):
    """
    Returns Mth element in sequence, where last sequence is number.

    >>> solver(['a', 'b', 3]) == None
    True
    >>> solver(['a', 1])
    'a'
    >>> solver(['a', 'b', 'c', 2])
    'b'
    >>> solver('a b c d 4'.split())
    'a'
    >>> solver('e f g h 2'.split())
    'g'

    :param seq: data to solve
    :type seq: list
    :return: char at position or None if out of range
    :rtype: basestring|None
    """
    position = int(seq[-1])
    if position > len(seq) -1:
        return None
    return seq[-(1+position)]

if __name__ == '__main__':
    with open(sys.argv[1]) as data:
        for result in filter(None, (solver(line.split()) for line in data)):
            print result