__author__ = 'zadoev@gmail.com'


import unittest

from solutions.sum_of_primes import main


class MainTestCase(unittest.TestCase):
    def test_primes_method(self):
        self.assertEquals([2, 3, 5, 7, 11], main.primes(12))

    def test_solver_for_small_number(self):
        self.assertEquals(sum([2, 3, 5, 7, 11]), main.solver(12))

    def test_ok(self):
        self.assertEquals(3682913, main.solver(7919 + 1))
