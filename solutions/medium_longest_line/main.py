__author__ = 'zadoev@gmail.com'

import sys


def solve(lines, limit):
    """
    >>> solve(['a', 'b'], 1)
    ['a']
    >>> solve(['a', 'aa', 'aaa'], 2)
    ['aaa', 'aa']

    :param lines:
    :type lines: list
    :param limit:
    :type limit: int
    :return:
    :rtype: list
    """
    return sorted(lines, key=len, reverse=True)[:limit]

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        limit = int(next(test_cases))
        print '\n'.join(solve(test_cases, limit)).rstrip()

