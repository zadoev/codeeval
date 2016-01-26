__author__ = 'zadoev@gmail.com'

import sys
from collections import Counter


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
    number = list(map(int, number))
    counts = Counter(number)
    return all(
        map(lambda x: counts[x[0]] == x[1], enumerate(number))
    )


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print(int(is_self_describing(line.rstrip())))
