__author__ = 'cd'

import unittest

from solutions.prime_palindrome import main


class HelpersTestCase(unittest.TestCase):

    def test_main_method_exists(self):
        """
        Import are ok, tests works, i can move on
        :return:
        :rtype:
        """
        self.assertTrue(callable(main.max_prime_palindrome))

    def test_primes_method(self):
        self.assertEquals([2,3,5,7], main.primes(10))

    def test_is_palindrome_ok(self):
        self.assertTrue(main.is_palindrome('aba'))

    def test_is_palindrome_ok_for_digits(self):
        self.assertTrue(main.is_palindrome(121))

    def test_is_palindrome_ko(self):
        self.assertFalse(main.is_palindrome('abav'))

    def test_max_prime_palindrome_for_10(self):
        self.assertEquals(7, main.max_prime_palindrome(10))

    def test_max_prime_palindrome_for_1000(self):
        self.assertEquals(929, main.max_prime_palindrome(1000))



