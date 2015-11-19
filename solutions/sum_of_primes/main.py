__author__ = 'zadoev@gmail.com'

# precalculated https://primes.utm.edu/lists/small/1000.txt
# if we don't know value we can incrementaly get it by calling primes ( not efficient)
THOUSANDTH_PRIME_VALUE = 7919


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
    for i in xrange(3, n+1, 2):
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


def solver(n):
    return sum(primes(n))

if __name__ == '__main__':
    print solver(THOUSANDTH_PRIME_VALUE + 1)