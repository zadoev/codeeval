__author__ = 'zadoev@gmail.com'

import sys


def solver(num, pos1, pos2):
    return (num >> (pos1 - 1) & 1) == (num >> (pos2 - 1) & 1)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print ['false', 'true'][solver(*map(int, line.split(',')))]