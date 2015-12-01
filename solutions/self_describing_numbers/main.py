__author__ = 'zadoev@gmail.com'

import sys
from collections import Counter
from itertools import imap


def is_self_describing(number):
    """
    Detects if number is self describing

    >>> is_self_describing('2020')
    True

    >>> is_self_describing('22')
    False

    >>> is_self_describing('1210')
    True

    :param number: string with number
    :type number: basestring
    :return: true if number self describing false otherwise
    :rtype: boolean
    """
    number = map(int, number)
    counts = Counter(number)

    return all(
        imap(lambda (pos, char): counts[pos] == char, enumerate(number))
    )


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print int(is_self_describing(line.rstrip()))
