import unittest

from solutions.fizz_buzz.main import calc, transplitter


class TestTransplitter(unittest.TestCase):
    def test_same(self):
        self.assertEquals('8', transplitter(3, 5, 8))

    def test_fizz(self):
        self.assertEquals('F', transplitter(2, 5, 8))

    def test_buzz(self):
        self.assertEquals('B', transplitter(3, 4, 8))

    def test_fizzbuzz(self):
        self.assertEquals('FB', transplitter(2, 4, 8))


class TestCalc(unittest.TestCase):
    def test_var1(self):
        x = 3
        y = 5
        n = 10
        self.assertEquals(
            ['1', '2', 'F', '4', 'B', 'F', '7', '8', 'F', 'B'],
            calc(x, y, n)
        )

    def test_var2(self):
        x = 2
        y = 7
        n = 15
        self.assertEquals(
            ['1', 'F', '3', 'F', '5', 'F', 'B', 'F', '9', 'F', '11', 'F', '13', 'FB', '15'],
            calc(x, y, n)
        )
