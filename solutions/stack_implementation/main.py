# -*- coding: utf-8 -*-
__author__ = 'zadoev@gmail.com'
"""
Write a program which implements a stack interface for integers. The interface
should have ‘push’ and ‘pop’ functions. Your task is to ‘push’ a series of
integers and then ‘pop’ and print every alternate integer.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains a
series of space delimited integers, one per line.

For example:

1 2 3 4
10 -2 3 4

OUTPUT SAMPLE:

Print to stdout every alternate space delimited integer, one per line.

For example:

4 2
4 -2
"""
import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            stack = line.split()

            for i in xrange(len(stack)):
                k = stack.pop()

                if i % 2 == 0:
                    print k,
            print