__author__ = 'zadoev@gmail.com'
"""
Credits: This challenge appeared in the Facebook Hacker Cup 2011.
A double-square number is an integer X which can be expressed as the sum of
two perfect squares. For example, 10 is a double-square because 10 = 3^2 + 1^2.
Your task in this problem is, given X, determine the number of ways in which
it can be written as the sum of two squares.

For example, 10 can only be written as 3^2 + 1^2 (we don't count 1^2 + 3^2 as
being different). On the other hand, 25 can be written as 5^2 + 0^2 or as 4^2
+ 3^2.
NOTE: Do NOT attempt a brute force approach. It will not work. The following
constraints hold:
0 <= X <= 2147483647
1 <= N <= 100

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. You
should first read an integer N, the number of test cases. The next N lines
will contain N values of X.

5
10
25
3
0
1
OUTPUT SAMPLE:

1
2
0
1
1

"""
import sys
import math


def solve(n):
    """
    >>> solve(5)
    1
    >>> solve(10)
    1
    >>> solve(25)
    2
    >>> solve(13)
    1
    >>> solve(3)
    0
    >>> solve(0)
    1
    >>> solve(1)
    1
    >>> solve(2147483647)  # i don't know answer, just test huge number bench
    0

    :param n: number to find solutions
    :type n: int
    :return: count of n representation in double squares
    :rtype: int
    """
    p = int(math.sqrt(n/2.0))
    total = 0

    for i in xrange(p+1):
        j = math.sqrt(n - i*i)

        if j == int(j):
            total += 1

    return total


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        count = int(next(test_cases).rstrip())
        for line in test_cases:
            print solve(int(line.rstrip()))
