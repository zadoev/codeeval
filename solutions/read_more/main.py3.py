__author__ = 'zadoev@gmail.com'

import sys

def trimmer(text):
    """
    Trim text

    >>> trimmer('a')
    'a'
    >>> trimmer('a' * 56)
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa... <Read More>'
    >>> trimmer('a' + ' ' * 30 + 'd' * 30)
    'a                             ... <Read More>'

    :param text: text to trim
    :rtype text: basestring
    :return:
    """
    if len(text) <= 55:
        return text

    text = text[:40]

    last_space = text.rfind(' ')

    if last_space != -1:
        text = text[0:last_space]

    return ''.join((text, '... <Read More>'))

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print(trimmer(line.strip()))