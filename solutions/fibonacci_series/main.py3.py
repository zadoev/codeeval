__author__ = 'cd'

import sys


def fib(n):
    """
    Returns fibonacci number for n

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(25)
    75025
    """
    if n < 2:
        return n

    a = 0
    b = 1

    for i in range(2, n+1):
        (a, b) = (b, a + b)

    return b

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print(fib(int(line.rstrip())))