"""
__author__ = "zadoev@gmail.com"

Used http://algolist.ru/search/lcs/simple_lcs.php
"""
import sys
from ctypes import c_uint


def solve(s1, s2):
    """
    Using dict to keep table, it takes less memory as tested in prev solutions


    >>> solve('ab', 'ab')
    'ab'

    >>> solve('cab', 'ab')
    'ab'

    >>> solve('qerty', '1q22e333r4444t555y666')
    'qerty'

    >>> solve('1q22e333r4444t555y666', 'qerty')
    'qerty'

    >>> solve('abc', 'def')
    ''

    :param s1:
    :param s2:
    :return:
    """
    # data = defaultdict(lambda: defaultdict(int))

    s1_len = len(s1)
    s2_len = len(s2)

    KInts = c_uint * (s2_len + 1)
    Mtrx = KInts * (s1_len + 3)
    matrix = Mtrx()

    for i in reversed(range(s1_len)):
        for j in reversed(range(s2_len)):
            if s1[i] == s2[j]:
                matrix[i][j] = 1 + matrix[i+1][j+1]
            else:
                matrix[i][j] = max(
                    matrix[i+1][j],
                    matrix[i][j+1]
                )

    s = []

    while i < s1_len and j < s2_len:
        if s1[i] == s2[j]:
            s.append(s1[i])
            i += 1
            j += 1
        elif matrix[i+1][j] >= matrix[i][j+1]:
            i += 1
        else:
            j += 1

    return ''.join(s)


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print solve(*line.rstrip().split(';'))