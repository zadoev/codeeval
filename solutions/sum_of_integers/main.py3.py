__author__ = 'zadoev@gmail.com'
"""
Write a program to determine the largest sum of contiguous integers in a list.

INPUT SAMPLE:

The first argument is a path to a filename containing a comma-separated
list of integers, one per line.

For example:

-10,2,3,-2,0,5,-15
2,3,-2,-1,10
OUTPUT SAMPLE:

Print to stdout the largest sum. In other words, of all the possible contiguous
subarrays for a given array, find the one with the largest sum, and
print that sum.

For example:

8
12

"""

import sys



def solve(seq):
    """
    Kadane's algorithm

    >>> solve([1])
    1
    >>> solve([-1,1])
    1
    >>> solve([-10,2,3,-2,0,5,-15])
    8
    >>> solve([2,3,-2,-1,10])
    12

    >>> solve([-1,-2,-3,-3])
    -1

    :param seq: sequence to find result
    :type seq: list
    :return: max sum in seq for any contiguous sub array
    :rtype: int
    """
    s = 0
    ans = seq[0]
    for i in seq:
        s += i
        ans = max(ans, s)
        s = max(s, 0)

    return ans


if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print(solve(list(map(int, line.rstrip().split(',')))))
