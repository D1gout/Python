import math
import unittest


def equation(a, b, c):
    if b == 0 and c != 0:
        return "Not real"
    if a == 0:
        if b != 0:
            x_l = c / b
            return round(x_l, 3)
        else:
            return "Not real"
    else:
        D = b * b - 4 * a * c
        if D >= 0:
            if D == 0:
                x = -b / (2 * a)
                return round(x, 3)
            else:
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                return round(x1, 3), round(x2, 3)
        else:
            return "Not real"


class TestEquation(unittest.TestCase):

    def test_not_real(self):
        self.assertEqual(equation(0, 0, 1), "Not real")

    def test_one_solution(self):
        self.assertEqual(equation(0, 2, 4), -2)

    def test_two_solutions(self):
        self.assertEqual(equation(1, 4, 3), (-3.0, -1.0))


if __name__ == '__main__':
    unittest.main()
