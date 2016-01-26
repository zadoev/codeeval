# encoding: utf-8

"""
__author__ = 'zadoev@gmail.com'

https://www.codeeval.com/open_challenges/35/

"""
import sys
import re

EMAIL_REGEX = re.compile('^"[a-z|A-Z|0-9|_|-|+|.|@]+"|[a-z|A-Z|0-9|_|-|+|.?]*'
                         '@{1}[a-z|0-9]+\.{1}[a-z|0-9|-]+\.?[a-z|0-9|-]{2,}')


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print(['false', 'true'][re.match(EMAIL_REGEX, line) is not None])
