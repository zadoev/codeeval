__author__ = 'zadoev@gmail.com'
"""
There are two strings: A and B. Print 1 if string B occurs at the end of
string A. Otherwise, print 0.

INPUT SAMPLE:

The first argument is a path to the input filename containing two
comma-delimited strings, one per line. Ignore all empty lines in the input file.

For example:

Hello World,World
Hello CodeEval,CodeEval
San Francisco,San Jose
OUTPUT SAMPLE:

Print 1 if the second string occurs at the end of the first string. Otherwise, print 0.

For example:

1
1
0
"""
import sys

bool_to_int = (0, 1)

if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            line = line.rstrip()
            if line:
                a, b = line.split(',')
                print(bool_to_int[a[-len(b):] == b])