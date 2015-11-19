__author__ = 'zadoev@gmail.com'

import timeit

from solutions.sum_of_primes.main import primes as primers_may_be_better
from solutions.prime_palindrome.main import primes as primes_original


print "may be better: {}".format(
    timeit.timeit(lambda: primers_may_be_better(1000), number=10000)
)

print "Original: {}".format(
    timeit.timeit(lambda: primes_original(1000), number=10000)
)