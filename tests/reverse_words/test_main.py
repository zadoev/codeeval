__author__ = 'zadoev@gmail.com'

import unittest

from solutions.reverse_words.main import data_generator, solver

from StringIO import StringIO


class DataGeneratorTestCase(unittest.TestCase):
    def test_file_with_single_row(self):

        stream = StringIO("first second")

        self.assertEquals([['first', 'second']], list(data_generator(stream)))

    def test_file_with_empty_row(self):
        stream = StringIO("first second\n\nhello world\n\n")

        self.assertEquals(
            [['first', 'second'], ['hello', 'world']],
            list(data_generator(stream))
        )


class SolverTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEquals('', solver([]))

    def test_ok(self):
        self.assertEquals('world hello', solver(['hello', 'world']))