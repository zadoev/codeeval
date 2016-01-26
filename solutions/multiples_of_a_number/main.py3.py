__author__ = 'zadoev@gmail.com'

import sys


def solver(x, n):
    step = 1
    r = n
    while x > r:
        step += 1
        r = n * step
    return r


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print(solver(*map(int, line.split(','))))