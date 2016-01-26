__author__ = 'zadoev@gmail.com'
"""
CHALLENGE DESCRIPTION:

You are given two strings. Determine if the second string is a substring of
the first (Do NOT use any substr type library function). The second string may
contain an asterisk(*) which should be treated as a regular expression i.e.
matches zero or more characters. The asterisk can be escaped by a \ char in
which case it should be interpreted as a regular '*' character. To summarize:
the strings can contain alphabets, numbers, * and \ characters.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. The
input file contains two comma delimited strings per line. E.g.

Hello,ell
This is good, is
CodeEval,C*Eval
Old,Young
OUTPUT SAMPLE:

If the second string is indeed a substring of the first, print out a 'true'
(lowercase), else print out a 'false'(lowercase), one per line. E.g.

true
true
true
false
print true if second string in first

"""
import re
import sys

REGEXP_BUILDER_PATTERN = re.compile(r'((?<!\\)\*)')


def reg_exp_builder(pattern):
    """
    builds regexp from input pattern

    >>> reg_exp_builder('')
    ''
    >>> reg_exp_builder('abc')
    'abc'
    >>> reg_exp_builder('C*Eval')
    'C.*?Eval'
    >>> reg_exp_builder('*Eval')
    '.*?Eval'
    >>> reg_exp_builder('C\\*Eval')
    'C\\\\*Eval'

    :param pattern: input for build pattern
    :type pattern: basestring
    :return: regexp expression
    :rtype: basestring
    """
    return REGEXP_BUILDER_PATTERN.sub('.*?', pattern)


def find_second_in_first(a, b):
    """
    Search if pattern b in a

    >>> find_second_in_first('Hello','ell')
    True
    >>> find_second_in_first('This is good', 'is')
    True
    >>> find_second_in_first('CodeEval', 'C*Eval')
    True
    >>> find_second_in_first('CodeEval', '*Eval')
    True
    >>> find_second_in_first('Old', 'Young')
    False
    >>> find_second_in_first('Old', '*')
    True
    >>> find_second_in_first('Old', 'Old*')
    True
    """

    return re.search(reg_exp_builder(b), a) is not None


if __name__ == '__main__':
    responses = ('false', 'true')
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print(responses[find_second_in_first(*line.rstrip().split(','))])
