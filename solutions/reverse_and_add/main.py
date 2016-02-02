"""
__author__ = "zadoev@gmail.com"

https://www.codeeval.com/open_challenges/45/
"""
import sys


def solve(num):
    """
    >>> solve('195')
    ('4', '9339')

    >>> solve('1')
    ('1', '2')

    :param num: digit to apply 196 algo
    :return: tuple with attempts and final palindrome
    """
    attempts = 1
    num_as_str = num
    num = int(num)
    while True:
        num += int(num_as_str[::-1])

        num_as_str = str(num)

        if num_as_str == num_as_str[::-1]:
            return str(attempts), num_as_str

        attempts += 1


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print ' '.join(solve(line.rstrip()))