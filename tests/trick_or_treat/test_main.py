__author__ = 'zadoev@gmail.com'

import unittest

from solutions.trick_or_treat import main


class ParseInputTestCase(unittest.TestCase):
    def test_has_func(self):
        self.assertTrue(callable(main.parse_input))

    def test_simple_input(self):
        line = 'Vampiries: 1, Zombies: 1, Witches: 1, Houses: 1'

        self.assertEqual(
            ({'Vampiries': 1, 'Zombies': 1, 'Witches': 1},1),
            main.parse_input(line)
        )

    def test_adv_input(self):
        line = 'Vampiries: 0, Zombies: 1, Witches: 12, Houses: 0'

        self.assertEqual(
            ({'Vampiries': 0, 'Zombies': 1, 'Witches': 12}, 0),
            main.parse_input(line)
        )


class SolveTestCase(unittest.TestCase):
    def test_zero_houses(self):
        self.assertEquals(0, main.solve({}, 0))

    def test_no_costumes_houses(self):
        self.assertEquals(0, main.solve({}, 1))

    def test_single_vampire_in_one_house(self):

        self.assertEquals(
            main.PRIZES[main.VAMPIRES],
            main.solve({main.VAMPIRES: 1}, 1)
        )

    def test_example1(self):
        line = 'Vampires: 1, Zombies: 1, Witches: 1, Houses: 1'
        costumes, houses = main.parse_input(line)

        self.assertEquals(4, main.solve(costumes, houses))

    def test_example2(self):
        line = 'Vampires: 3, Zombies: 2, Witches: 1, Houses: 10'
        costumes, houses = main.parse_input(line)

        self.assertEquals(36, main.solve(costumes, houses))

    def test_zero_vampires(self):

        self.assertEquals(0, main.solve({main.VAMPIRES:0}, 1))