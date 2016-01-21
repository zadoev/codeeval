from __future__ import print_function
__author__ = 'zadoev@gmail.com'


def mult_table_gen(cols, rows, width):
    """

    >>> ''.join(mult_table_gen(1, 1, 4))
    '   1\\n'

    >>> ''.join(mult_table_gen(2, 2, 4))
    '   1   2\\n   2   4\\n'

    :param cols: columns number
    :type cols:  int
    :param rows: rows number
    :type rows: int
    :param width: format width of item
    :type width: int
    :return: yield next value to print with \n as extra value
    :rtype: str
    """
    for r in range(1, cols+1):
        for c in range(1, rows+1):
            yield str(r*c).rjust(width)
        yield '\n'


if __name__ == '__main__':
    for v in mult_table_gen(12, 12, width=4):
        print(v, end='')


