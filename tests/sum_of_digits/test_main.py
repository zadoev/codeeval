__author__ = 'zadoev@gmail.com'

import unittest

from solutions.sum_of_digits import main


class SolverTestCase(unittest.TestCase):
    def test_single(self):
        self.assertEquals(7, main.solver('7'))

    def test_single(self):
        self.assertEquals(45, main.solver('123456789'))
