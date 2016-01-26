__author__ = 'zadoev@gmail.com'
"""
CHALLENGE DESCRIPTION:

Write a program which prints all the permutations of a string in alphabetical
order. We consider that digits < upper case letters < lower case letters.
The sorting should be performed in ascending order.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains
input strings, one per line.

For example:

hat
abc
Zu6
OUTPUT SAMPLE:

Print to stdout the permutations of the string separated by comma,
in alphabetical order.

For example:

aht,ath,hat,hta,tah,tha
abc,acb,bac,bca,cab,cba
6Zu,6uZ,Z6u,Zu6,u6Z,uZ6
"""

import sys

from itertools import permutations


def solve(in_str):
    """
    Returns sorted string permutations

    >>> solve('hat')
    'aht,ath,hat,hta,tah,tha'
    >>> solve('Zu6')
    '6Zu,6uZ,Z6u,Zu6,u6Z,uZ6'
    >>> solve('abc')
    'abc,acb,bac,bca,cab,cba'

    :param in_str: input
    :type in_str: basestring
    :return: solution
    :rtype: basestring
    """

    return ','.join(sorted(map(lambda x: ''.join(x),permutations(in_str))))


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print(solve(line.rstrip()))
