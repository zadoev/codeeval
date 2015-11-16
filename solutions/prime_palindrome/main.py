__author__ = 'zadoev@gmail.com'

def primes(n):
    """
    http://stackoverflow.com/questions/567222/simple-prime-generator-in-python

    :param n:
    :type n: int
    :return: primes before n
    :rtype: int[]
    """
    odds = range(3, n+1, 2)
    # step q + q optimization, evens already cut off
    sieve = set(sum([range(q*q, n+1, q+q) for q in odds],[]))
    return [2] + [p for p in odds if p not in sieve]


def is_palindrome(n):
    """
    Or may be better to find with
    :param n:
    :type n: str|int
    :return: true if n is palindrome false otherwise
    :rtype: bool
    """
    return str(n) == str(n)[::-1]


def max_prime_palindrome(n):
    """
    Returns max prime palindrome before n
    :param n:
    :type n:
    :return:
    :rtype:
    """
    sorted_primes = sorted(primes(n), reverse=True)

    for i in sorted_primes:
        if is_palindrome(i):
            return i

if __name__ == '__main__':
    print max_prime_palindrome(1000)