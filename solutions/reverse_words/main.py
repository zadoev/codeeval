__author__ = 'zadoev@gmail.com'

import sys


def data_generator(stream):
    for line in stream:
        if not line.strip():
            continue
        yield line.split()


def solver(seq):
    return ' '.join(reversed(seq))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for words in data_generator(test_cases):
            print solver(words)