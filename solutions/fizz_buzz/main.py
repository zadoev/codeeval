import sys

from functools import partial


def transplitter(x, y, i):
    res = ''
    if i % x == 0:
        res = 'F'

    if i % y == 0:
        res += 'B'

    return res or str(i)


def calc(x, y, n):
    t = partial(transplitter,x, y)
    return map(t, xrange(1, n+1))

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:
        # ignore test if it is an empty line
        if not test.strip():
            continue
        # 'test' represents the test case, do something with it
        try:
            (x, y, n) = map(lambda x:int(x.strip()), test.split(' '))
            print ' '.join(calc(x,y,n))
        except ValueError:
            continue

    test_cases.close()