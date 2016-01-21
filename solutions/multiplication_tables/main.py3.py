"""
https://www.codeeval.com/open_challenges/23/

"""
__author__ = 'zadoev@gmail.com'


def mult_table_gen(cols: int, rows: int , width: int):
    """

    >>> ''.join(mult_table_gen(1, 1, 4))
    '   1\\n'

    >>> ''.join(mult_table_gen(2, 2, 4))
    '   1   2\\n   2   4\\n'

    :param cols: columns number
    :param rows: rows number
    :param width: format width of item
    :return: yield next value to print with \n as extra value
    """
    for r in range(1, cols+1):
        for c in range(1, rows+1):
            yield str(r*c).rjust(width)
        yield '\n'


if __name__ == '__main__':
    for v in mult_table_gen(12, 12, width=4):
        print(v, end='')


