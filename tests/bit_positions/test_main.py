__author__ = 'zadoev@gmail.com'

import unittest

from solutions.bit_positions import main


class SolverTestCase(unittest.TestCase):

    def test_zeros(self):
        self.assertTrue(main.solver(0, 1, 200))

    def test_eq(self):
        self.assertTrue(main.solver(11, 1, 1))

    def test_out_of_range(self):
        self.assertTrue(main.solver(1, 11, 11))

    def test_diff(self):
        self.assertFalse(main.solver(2, 1, 2))

    def test_sample1(self):
        self.assertTrue(main.solver(86, 2, 3))

    def test_sample2(self):
        self.assertFalse(main.solver(125, 1, 2))

