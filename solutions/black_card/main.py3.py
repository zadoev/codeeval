"""
https://www.codeeval.com/open_challenges/222
"""
import sys


def parse(raw_data):
    names, number = map(lambda x: x.strip(), raw_data.split('|'))
    return names.split(' '), int(number)


def solver(names, number):
    """
    Detect winner

    :param names:
    :type names: list
    :param number:
    :type number:
    :return:
    :rtype:
    """
    length = len(names)
    names_pop = names.pop
    while length > 1:
        names_pop(number % length - 1)
        length -= 1
    return names[0]


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print(solver(*parse(line)))