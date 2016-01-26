"""
CHALLENGE DESCRIPTION:

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.
Each line in this file contains a positive integer which is the total
number of stairs.
Ignore all empty lines. E.g.

10
20
OUTPUT SAMPLE:

Print out the number of ways to climb to the top of the staircase. E.g.

89
10946
Constraints:
The total number of stairs is <= 1000
"""
import sys


def fib(n):
    """
    Solution from fibonacci series

    Returns fibonacci number for n

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(25)
    75025

    :param n:
    :type n: int

    :return: fibonacci number for n
    """
    if n < 2:
        return n

    a = 0
    b = 1

    for i in range(2, n+1):
        (a, b) = (b, a + b)

    return b

"""
Solutions if g(n) = fib(n+1)

Prove:
imaging that if i have all solutions before n and i want to find solution
for n

i can jump from n-1 to n in this case i have f(n-1) solutions count
i can jump from n-2 to n in this case i have f(n-2) solutions
so total i have f(n-2) + f(n-1) solutions and it's fibonnacci numbers

now need find initial values

for n = 0 i have 0 solutions
for n = 1 i have 0 solution (i'm on top already)
for n=1 i have 1 solution, just up for 1
for n=2 i have 2 solutions (11, and 2)
for n=3 i have 3 solutions (111, 21, 12)

so i need calculate fib(n+1) to get answer
"""

if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            print(fib(int(line.rstrip())+1))
