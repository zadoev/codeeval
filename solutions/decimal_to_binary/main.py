__author__ = 'zadoev@gmail.com'
"""
You are given a decimal (base 10) number, print its binary representation.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename containing
decimal numbers greater or equal to 0, one per line.

Ignore all empty lines.

For example:

2
10
67
OUTPUT SAMPLE:

Print the binary representation, one per line.

For example:

10
1010
1000011

"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            data = line.rstrip()
            if data:
                print bin(int(data))[2:]
