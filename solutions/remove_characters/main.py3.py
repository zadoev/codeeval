__author__ = 'zadoev@gmail.com'
"""
Write a program which removes specific characters from a string.

INPUT SAMPLE:

The first argument is a path to a file. The file contains the source strings and
the characters that need to be scrubbed. Each source string and characters
you need to scrub are delimited by comma.

For example:

how are you, abc
hello world, def
OUTPUT SAMPLE:

Print to stdout the scrubbed strings, one per line. Ensure that there are no
trailing empty spaces on each line you print.

For example:

how re you
hllo worl

"""
import sys
from string import ascii_letters


tab = str.maketrans(ascii_letters, ascii_letters)


def solve(tongue, denied):
    """
    >>> ''.join(solve('abc', 'def'))
    'abc'
    >>> ''.join(solve('abc', 'b'))
    'ac'

    :param tongue: input line
    :type tongue: basestring
    :param denied: characters to remove
    :type denied: basestring
    :return: line without chars from denied
    :rtype: basestring
    """
    return filter(lambda x: x not in denied, tongue)


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print(''.join(solve(*map(str.strip, line.split(',')))))
