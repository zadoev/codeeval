__author__ = 'zadoev@gmail.com'

import unittest

from solutions.multiples_of_a_number import main

from solutions.multiples_of_a_number import bench

class SolverTestCase(unittest.TestCase):
    def test_gt(self):
        self.assertEquals(16, main.solver(13, 8))
        self.assertEquals(32, main.solver(17, 16))


        self.assertEquals(16, bench.solver2(13, 8))
        self.assertEquals(32, bench.solver2(17, 16))

    def test_gt2(self):
        self.assertEquals(24, main.solver(17, 8))

        self.assertEquals(24, bench.solver2(17, 8))

    def test_lt(self):
        self.assertEquals(8, main.solver(1, 8))

        self.assertEquals(8, bench.solver2(1, 8))

