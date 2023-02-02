import unittest


class TestEquation(unittest.TestCase):
    def test_a_eq_0(self):
        self.assertEqual(equation(0, 4, 8), -2)

    def test_D_eq_0(self):
        self.assertEqual(equation(2, 4, 2), -1)

    def test_D_gt_0(self):
        self.assertEqual(equation(1, -5, 6), (3.0, 2.0))

    def test_D_lt_0(self):
        self.assertEqual(equation(1, 5, 6), "Not real")
