# -*- coding: utf-8 -*-

__author__ = 'zadoev@gmail.com'
"""
PREFIX EXPRESSIONS
CHALLENGE DESCRIPTION:

You are given a prefix expression. Write a program which evaluates it.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains one
prefix expression per line.

For example:

* + 2 3 4
Your program should read this file and insert it into any data structure you
like. Traverse this data structure and evaluate the prefix expression.
Each token is delimited by a whitespace. You may assume that sum ‘+’,
multiplication ‘*’ and division ‘/’ are the only valid operators appearing in
the test data.

OUTPUT SAMPLE:

Print to stdout the output of the prefix expression, one per line.

For example:



1
20
CONSTRAINTS:

The evaluation result will always be an integer ≥ 0.
The number of the test cases is ≤ 40.
"""

from operator import add, mul, div
import sys


def solve(seq):
    """
    >>> solve(['*','+', '2', '3', '4'])
    20

    :param seq: list with prefix expression
    :type seq: list
    :return: result of evaluation
    :rtype: int
    """
    stack = []

    operators = {
        '+': add,
        '*': mul,
        '/': div,
    }

    for i in reversed(seq):
        if i.isdigit():
            stack.append(i)
        else:
            operand1 = float(stack.pop())
            operand2 = float(stack.pop())
            stack.append(operators[i](operand1, operand2))

    return int(stack.pop())


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print solve(line.split())
