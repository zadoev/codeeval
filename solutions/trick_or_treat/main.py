__author__ = 'zadoev@gmail.com'

import string
import sys

VAMPIRES = 'Vampires'
ZOMBIES = 'Zombies'
WITCHES = 'Witches'

PRIZES = {
    VAMPIRES: 3,
    ZOMBIES: 4,
    WITCHES: 5
}


def parse_input(input_line):
    # split each string by , and get data list each value str('key: val')
    data = map(string.strip, input_line.split(','))
    # make dict from data list like {'Vampires': 1, 'Houses': 2}
    data = {k: int(v) for k, v in map(lambda i: i.split(': '), data)}
    houses = data.pop('Houses')
    return data, houses


def solve(costumes, houses):

    children = sum(costumes.values())

    if children == 0:
        return 0

    return sum([PRIZES[k]*v for k, v in costumes.items()]) * houses/children


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print solve(*parse_input(line))