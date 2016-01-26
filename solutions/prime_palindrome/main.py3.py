__author__ = 'zadoev@gmail.com'

def primes(n):
    """
    http://habrahabr.ru/post/122538/

    4x faster then used in prime_palindrome
    :param n:
    :type n:
    :return:
    :rtype:
    """
    lst = [2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


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
    print(max_prime_palindrome(1000))