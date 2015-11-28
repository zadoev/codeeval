__author__ = 'cd'

import sys
from itertools import imap

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        print sum(imap(int, test_cases))
