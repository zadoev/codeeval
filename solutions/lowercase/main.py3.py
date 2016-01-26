__author__ = 'zadoev@gmail.com'

import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print(line.lower(), end='')
