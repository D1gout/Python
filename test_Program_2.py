import Program_2
import unittest


class Equation_case(unittest.TestCase):
    def test_1(self):
        self.assertTupleEqual((0.257, -2.591), Program_2.equation(3, 7, -2))

    def test_2(self):
        self.assertTupleEqual((0.175, -2.852), Program_2.equation(3.4, 9.1, -1.7))

    def test_3(self):
        self.assertTupleEqual((-0.878, 0.878), Program_2.equation(-3.72, 0, 2.87))

    def test_4(self):
        self.assertEqual(-3.417, Program_2.equation(0, 3.6, 12.3))

    def test_5(self):
        self.assertTupleEqual((0.000, -0.688), Program_2.equation(9.3, 6.4, 0))

    def test_6(self):
        self.assertEqual("Not real", Program_2.equation(2, 2, 1))
