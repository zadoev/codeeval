__author__ = 'zadoev@gmail.com'

import unittest

from solutions.da_vyncy import main


class SolverTestCase(unittest.TestCase):
    def test_solve(self):
        solver = main.Solver([
            'O draconia',
            'conian devil! Oh la',
            'h lame sa',
            'saint!'
        ])

        self.assertEquals(
            'O draconian devil! Oh lame saint!',
            solver.solve()
        )

    def test_solve2(self):
        data = 'm quaerat voluptatem.;pora incidunt ut labore et d;, consectetur, adipisci velit;olore magnam aliqua;idunt ut labore et dolore magn;uptatem.;i dolorem ipsum qu;iquam quaerat vol;psum quia dolor sit amet, consectetur, a;ia dolor sit amet, conse;squam est, qui do;Neque porro quisquam est, qu;aerat voluptatem.;m eius modi tem;Neque porro qui;, sed quia non numquam ei;lorem ipsum quia dolor sit amet;ctetur, adipisci velit, sed quia non numq;unt ut labore et dolore magnam aliquam qu;dipisci velit, sed quia non numqua;us modi tempora incid;Neque porro quisquam est, qui dolorem i;uam eius modi tem;pora inc;am al'

        solver = main.Solver(data.split(';'))

        self.assertEquals(
            'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.',
            solver.solve()
        )