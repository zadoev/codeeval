__author__ = 'zadoev@gmail.com'

import sys

"""
https://www.codeeval.com/open_challenges/47/
"""


def solve(left, right):
    """
    >>> solve(9, 22)
    69
    >>> solve(9, 35)
    183
    >>> solve(100, 200)
    2551
    >>> solve(1, 1000)
    250000
    """

    cnt, result, length = 0, 0, 0
    non_palindrome_counts = []

    for i in xrange(left, right+1):
        s = str(i)
        if s == s[::-1]:
            cnt += 1
            non_palindrome_counts.append(length)
            result += length * (1 + length)/2
            length = 0
        else:
            length += 1

    # tail
    result += length * (1 + length)/2
    non_palindrome_counts.append(length)

    # testing even count of palindromes with closest non palindromes
    k = 1
    while k <= cnt:

        for i in xrange(0, cnt-k):
            result += non_palindrome_counts[i]  # left non palindrome counts
            result += non_palindrome_counts[i+k+1]  # right
            # combination left and right including odd count of palindromes
            result += non_palindrome_counts[i] * non_palindrome_counts[i+k+1]

        k += 2  # only even palidindrome count

    a1 = 1 + cnt % 2
    an = cnt - 1

    return (cnt//2) * (a1 + an)/2 + result


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print solve(*map(int, line.split()))