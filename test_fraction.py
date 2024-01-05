import unittest
from fractionCorrection import Fraction


class TestFraction(unittest.TestCase):
    def test_init(self):
        f = Fraction(1, 2)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        f_2 = Fraction(2, 4)
        self.assertEqual(f_2.numerator, 1)
        self.assertEqual(f_2.denominator, 2)

        f_3 = Fraction(4, 2)
        self.assertEqual(f_3.numerator, 2)
        self.assertEqual(f_3.denominator, 1)

        f_4 = Fraction(11, 7)
        self.assertEqual(f_4.numerator, 11)
        self.assertEqual(f_4.denominator, 7)

        f_5 = Fraction(0, 7)
        self.assertEqual(f_5.numerator, 0)
        self.assertEqual(f_5.denominator, 7)

    def test_fractionNegatives(self):
        f = Fraction(-1, 2)
        self.assertEqual(f.numerator, -1)
        self.assertEqual(f.denominator, 2)

        f2 = Fraction(-1, -2)
        self.assertEqual(f2.numerator, 1)
        self.assertEqual(f2.denominator, 2)

    def test_fractionPasCorrectes(self):
        with self.assertRaises(TypeError):
            Fraction(1.5, 2)

        with self.assertRaises(TypeError):
            Fraction(1, 2.2)

        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)


class TestStrMixed(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Fraction(1, 2)), '1/2')

        self.assertEqual(str(Fraction(-2, 3)), '-2/3')

        self.assertEqual(str(Fraction(4, 2)), '2')

        self.assertEqual(str(Fraction(10, 10)), '1')

    def test_asMixed(self):
        self.assertEqual(Fraction(7, 2).as_mixed_number(), '3 + 1/2')

        self.assertEqual(Fraction(-7, 2).as_mixed_number(), '-3 + 1/2')

        self.assertEqual(Fraction(0, 2).as_mixed_number(), '0')


class TestAddition(unittest.TestCase):
    def setUp(self):
        self.f = Fraction(1, 3)
        self.f_2 = Fraction(2, 6)
        self.f_3 = Fraction(-1, 5)
        self.f_4 = Fraction(7, 1)
        self.f_5 = Fraction(5, 5)
        self.f_6 = Fraction(-2, 5)

    def test_additionPositive(self):
        self.assertEqual(str(self.f + self.f_2), '2/3')

        self.assertEqual(str(self.f + self.f_4), '7 + 1/3')

        self.assertEqual(str(self.f_2 + self.f_5), '1 + 1/3')

    def test_additionNegative(self):
        self.assertEqual(str(self.f + self.f_3), '2/15')

        self.assertEqual(str(self.f_3 + self.f_4), '6 + 4/5')

        self.assertEqual(str(self.f_6 + self.f_3), '-3/5')


class TestDivision(unittest.TestCase):
    def test_divisionPositive(self):
        self.assertEqual(str(Fraction(1, 2) / Fraction(1, 2)), '1')
        self.assertEqual(str(Fraction(2, 2) / Fraction(1, 2)), '2')
        self.assertEqual(str(Fraction(7, 4) / Fraction(3, 2)), '1 + 1/6')

    def test_divisionNegative(self):
        self.assertEqual(str(Fraction(-1, 2) / Fraction(1, 2)), '-1')
        self.assertEqual(str(Fraction(-3, 2) / Fraction(-1, 3)), '4 + 1/2')

    def test_divisionZerroDivision(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2)/Fraction(0, 1)

        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 2)/Fraction(2, 1)


class TestEqu(unittest.TestCase):
    def test_equ(self):
        self.assertEqual(Fraction(1, 3) == Fraction(2, 6), True)
        self.assertEqual(Fraction(7, 2) == Fraction(-7, 2), False)
        self.assertEqual(Fraction(-1, 5) == Fraction(1, -5), True)
        self.assertEqual(Fraction(-1, -5) == Fraction(1, 5), True)


class TestIsInteger(unittest.TestCase):
    def test_estUnEntier(self):
        self.assertTrue(Fraction(2, 2).is_integer())
        self.assertTrue(Fraction(9, 3).is_integer())
        self.assertTrue(Fraction(-8, 4).is_integer())
        self.assertTrue(Fraction(0, 2).is_integer())

    def test_pasUnEntier(self):
        self.assertFalse(Fraction(1, 2).is_integer())
        self.assertFalse(Fraction(-7, 3).is_integer())


class TestIsProper(unittest.TestCase):
    def test_isProper(self):
        self.assertTrue(Fraction(1, 3).is_proper())
        self.assertTrue(Fraction(-2, 5).is_proper())
        self.assertFalse(Fraction(4, 1).is_proper())


class TestIsAdjacent(unittest.TestCase):
    def test_isAdjacent(self):
        self.assertTrue(Fraction(2, 1).is_adjacent_to(Fraction(1, 1)))
        self.assertFalse(Fraction(2, 7).is_adjacent_to(Fraction(1, 3)))


if __name__ == '__main__':
    unittest.main()
