__author__ = 'zadoev@gmail.com'

import unittest


from solutions.black_card import main


class ParseTestCase(unittest.TestCase):
    def test_parse_case1(self):
        line = 'silver john | 2'

        self.assertEquals((['silver', 'john'], 2), main.parse(line))

    def test_parse_extra_spaces(self):
        line = ' silver john  |  4 '

        self.assertEquals((['silver', 'john'], 4), main.parse(line))

    def test_parse_with_eol(self):
        line = " silver john  |  4\r\n"

        self.assertEquals((['silver', 'john'], 4), main.parse(line))


class SolverTestCase(unittest.TestCase):
    def test_simple(self):
        names = ['a', 'b']
        number = 1

        self.assertEquals('b', main.solver(names, number))

    def test_number_gt_then_names_count(self):
        names = ['a', 'b', 'c']
        number = 4

        self.assertEquals('b', main.solver(names, number))

    def test_example1(self):
        names = ['John', 'Sara', 'Tom', 'Susan']
        number = 4

        self.assertEquals('Sara', main.solver(names, number))

    def test_example2(self):
        names = ['John', 'Tom', 'Mary']
        number = 5

        self.assertEquals('Mary', main.solver(names, number))