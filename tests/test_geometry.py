"""Автоматические unit-тесты геометрической библиотеки.

Тесты написаны на unittest: каждый сценарий является отдельным методом
класса-наследника unittest.TestCase.
"""

import math
import unittest

from circle import area as circle_area
from circle import circumference
from square import area as square_area
from square import perimeter



class GeometryValidInputTests(unittest.TestCase):
    """Проверки корректных значений и математических результатов."""


    def test_circle_area_valid_01(self):
        result = circle_area(0)
        self.assertAlmostEqual(result, 0.0, places=7)


    def test_circle_area_valid_02(self):
        result = circle_area(1)
        self.assertAlmostEqual(result, 3.141592653589793, places=7)


    def test_circle_area_valid_03(self):
        result = circle_area(2)
        self.assertAlmostEqual(result, 12.566370614359172, places=7)


    def test_circle_area_valid_04(self):
        result = circle_area(3)
        self.assertAlmostEqual(result, 28.274333882308138, places=7)


    def test_circle_area_valid_05(self):
        result = circle_area(4)
        self.assertAlmostEqual(result, 50.26548245743669, places=7)


    def test_circle_area_valid_06(self):
        result = circle_area(5)
        self.assertAlmostEqual(result, 78.53981633974483, places=7)


    def test_circle_area_valid_07(self):
        result = circle_area(0.5)
        self.assertAlmostEqual(result, 0.7853981633974483, places=7)


    def test_circle_area_valid_08(self):
        result = circle_area(1.5)
        self.assertAlmostEqual(result, 7.0685834705770345, places=7)


    def test_circle_area_valid_09(self):
        result = circle_area(2.5)
        self.assertAlmostEqual(result, 19.634954084936208, places=7)


    def test_circle_area_valid_10(self):
        result = circle_area(10)
        self.assertAlmostEqual(result, 314.1592653589793, places=7)


    def test_circle_area_valid_11(self):
        result = circle_area(12.25)
        self.assertAlmostEqual(result, 471.4352475793183, places=7)


    def test_circle_area_valid_12(self):
        result = circle_area(100)
        self.assertAlmostEqual(result, 31415.926535897932, places=7)


    def test_circle_area_valid_13(self):
        result = circle_area(0.001)
        self.assertAlmostEqual(result, 3.1415926535897933e-06, places=7)


    def test_circle_area_valid_14(self):
        result = circle_area(7.75)
        self.assertAlmostEqual(result, 188.69190875623696, places=7)


    def test_circle_area_valid_15(self):
        result = circle_area(25)
        self.assertAlmostEqual(result, 1963.4954084936207, places=7)


    def test_circle_circumference_valid_01(self):
        result = circumference(0)
        self.assertAlmostEqual(result, 0.0, places=7)


    def test_circle_circumference_valid_02(self):
        result = circumference(1)
        self.assertAlmostEqual(result, 6.283185307179586, places=7)


    def test_circle_circumference_valid_03(self):
        result = circumference(2)
        self.assertAlmostEqual(result, 12.566370614359172, places=7)


    def test_circle_circumference_valid_04(self):
        result = circumference(3)
        self.assertAlmostEqual(result, 18.84955592153876, places=7)


    def test_circle_circumference_valid_05(self):
        result = circumference(4)
        self.assertAlmostEqual(result, 25.132741228718345, places=7)


    def test_circle_circumference_valid_06(self):
        result = circumference(5)
        self.assertAlmostEqual(result, 31.41592653589793, places=7)


    def test_circle_circumference_valid_07(self):
        result = circumference(0.5)
        self.assertAlmostEqual(result, 3.141592653589793, places=7)


    def test_circle_circumference_valid_08(self):
        result = circumference(1.5)
        self.assertAlmostEqual(result, 9.42477796076938, places=7)


    def test_circle_circumference_valid_09(self):
        result = circumference(2.5)
        self.assertAlmostEqual(result, 15.707963267948966, places=7)


    def test_circle_circumference_valid_10(self):
        result = circumference(10)
        self.assertAlmostEqual(result, 62.83185307179586, places=7)


    def test_circle_circumference_valid_11(self):
        result = circumference(12.25)
        self.assertAlmostEqual(result, 76.96902001294993, places=7)


    def test_circle_circumference_valid_12(self):
        result = circumference(100)
        self.assertAlmostEqual(result, 628.3185307179587, places=7)


    def test_circle_circumference_valid_13(self):
        result = circumference(0.001)
        self.assertAlmostEqual(result, 0.006283185307179587, places=7)


    def test_circle_circumference_valid_14(self):
        result = circumference(7.75)
        self.assertAlmostEqual(result, 48.69468613064179, places=7)


    def test_circle_circumference_valid_15(self):
        result = circumference(25)
        self.assertAlmostEqual(result, 157.07963267948966, places=7)


    def test_square_area_valid_01(self):
        result = square_area(0)
        self.assertEqual(result, 0)


    def test_square_area_valid_02(self):
        result = square_area(1)
        self.assertEqual(result, 1)


    def test_square_area_valid_03(self):
        result = square_area(2)
        self.assertEqual(result, 4)


    def test_square_area_valid_04(self):
        result = square_area(3)
        self.assertEqual(result, 9)


    def test_square_area_valid_05(self):
        result = square_area(4)
        self.assertEqual(result, 16)


    def test_square_area_valid_06(self):
        result = square_area(5)
        self.assertEqual(result, 25)


    def test_square_area_valid_07(self):
        result = square_area(0.5)
        self.assertEqual(result, 0.25)


    def test_square_area_valid_08(self):
        result = square_area(1.5)
        self.assertEqual(result, 2.25)


    def test_square_area_valid_09(self):
        result = square_area(2.5)
        self.assertEqual(result, 6.25)


    def test_square_area_valid_10(self):
        result = square_area(10)
        self.assertEqual(result, 100)


    def test_square_area_valid_11(self):
        result = square_area(12.25)
        self.assertEqual(result, 150.0625)


    def test_square_area_valid_12(self):
        result = square_area(100)
        self.assertEqual(result, 10000)


    def test_square_area_valid_13(self):
        result = square_area(0.001)
        self.assertEqual(result, 1e-06)


    def test_square_area_valid_14(self):
        result = square_area(7.75)
        self.assertEqual(result, 60.0625)


    def test_square_area_valid_15(self):
        result = square_area(25)
        self.assertEqual(result, 625)


    def test_square_perimeter_valid_01(self):
        result = perimeter(0)
        self.assertEqual(result, 0)


    def test_square_perimeter_valid_02(self):
        result = perimeter(1)
        self.assertEqual(result, 4)


    def test_square_perimeter_valid_03(self):
        result = perimeter(2)
        self.assertEqual(result, 8)


    def test_square_perimeter_valid_04(self):
        result = perimeter(3)
        self.assertEqual(result, 12)


    def test_square_perimeter_valid_05(self):
        result = perimeter(4)
        self.assertEqual(result, 16)


    def test_square_perimeter_valid_06(self):
        result = perimeter(5)
        self.assertEqual(result, 20)


    def test_square_perimeter_valid_07(self):
        result = perimeter(0.5)
        self.assertEqual(result, 2.0)


    def test_square_perimeter_valid_08(self):
        result = perimeter(1.5)
        self.assertEqual(result, 6.0)


    def test_square_perimeter_valid_09(self):
        result = perimeter(2.5)
        self.assertEqual(result, 10.0)


    def test_square_perimeter_valid_10(self):
        result = perimeter(10)
        self.assertEqual(result, 40)


    def test_square_perimeter_valid_11(self):
        result = perimeter(12.25)
        self.assertEqual(result, 49.0)


    def test_square_perimeter_valid_12(self):
        result = perimeter(100)
        self.assertEqual(result, 400)


    def test_square_perimeter_valid_13(self):
        result = perimeter(0.001)
        self.assertEqual(result, 0.004)


    def test_square_perimeter_valid_14(self):
        result = perimeter(7.75)
        self.assertEqual(result, 31.0)


    def test_square_perimeter_valid_15(self):
        result = perimeter(25)
        self.assertEqual(result, 100)



class GeometryInvalidInputTests(unittest.TestCase):
    """Проверки некорректных типов, отрицательных и нечисловых значений."""


    def test_circle_area_rejects_string(self):
        with self.assertRaises(TypeError):
            circle_area('abc')


    def test_circle_circumference_rejects_string(self):
        with self.assertRaises(TypeError):
            circumference('abc')


    def test_square_area_rejects_string(self):
        with self.assertRaises(TypeError):
            square_area('abc')


    def test_square_perimeter_rejects_string(self):
        with self.assertRaises(TypeError):
            perimeter('abc')


    def test_circle_area_rejects_empty_string(self):
        with self.assertRaises(TypeError):
            circle_area('')


    def test_circle_circumference_rejects_empty_string(self):
        with self.assertRaises(TypeError):
            circumference('')


    def test_square_area_rejects_empty_string(self):
        with self.assertRaises(TypeError):
            square_area('')


    def test_square_perimeter_rejects_empty_string(self):
        with self.assertRaises(TypeError):
            perimeter('')


    def test_circle_area_rejects_none(self):
        with self.assertRaises(TypeError):
            circle_area(None)


    def test_circle_circumference_rejects_none(self):
        with self.assertRaises(TypeError):
            circumference(None)


    def test_square_area_rejects_none(self):
        with self.assertRaises(TypeError):
            square_area(None)


    def test_square_perimeter_rejects_none(self):
        with self.assertRaises(TypeError):
            perimeter(None)


    def test_circle_area_rejects_boolean_true(self):
        with self.assertRaises(TypeError):
            circle_area(True)


    def test_circle_circumference_rejects_boolean_true(self):
        with self.assertRaises(TypeError):
            circumference(True)


    def test_square_area_rejects_boolean_true(self):
        with self.assertRaises(TypeError):
            square_area(True)


    def test_square_perimeter_rejects_boolean_true(self):
        with self.assertRaises(TypeError):
            perimeter(True)


    def test_circle_area_rejects_boolean_false(self):
        with self.assertRaises(TypeError):
            circle_area(False)


    def test_circle_circumference_rejects_boolean_false(self):
        with self.assertRaises(TypeError):
            circumference(False)


    def test_square_area_rejects_boolean_false(self):
        with self.assertRaises(TypeError):
            square_area(False)


    def test_square_perimeter_rejects_boolean_false(self):
        with self.assertRaises(TypeError):
            perimeter(False)


    def test_circle_area_rejects_complex(self):
        with self.assertRaises(TypeError):
            circle_area(2 + 3j)


    def test_circle_circumference_rejects_complex(self):
        with self.assertRaises(TypeError):
            circumference(2 + 3j)


    def test_square_area_rejects_complex(self):
        with self.assertRaises(TypeError):
            square_area(2 + 3j)


    def test_square_perimeter_rejects_complex(self):
        with self.assertRaises(TypeError):
            perimeter(2 + 3j)


    def test_circle_area_rejects_list(self):
        with self.assertRaises(TypeError):
            circle_area([2])


    def test_circle_circumference_rejects_list(self):
        with self.assertRaises(TypeError):
            circumference([2])


    def test_square_area_rejects_list(self):
        with self.assertRaises(TypeError):
            square_area([2])


    def test_square_perimeter_rejects_list(self):
        with self.assertRaises(TypeError):
            perimeter([2])


    def test_circle_area_rejects_tuple(self):
        with self.assertRaises(TypeError):
            circle_area((2,))


    def test_circle_circumference_rejects_tuple(self):
        with self.assertRaises(TypeError):
            circumference((2,))


    def test_square_area_rejects_tuple(self):
        with self.assertRaises(TypeError):
            square_area((2,))


    def test_square_perimeter_rejects_tuple(self):
        with self.assertRaises(TypeError):
            perimeter((2,))


    def test_circle_area_rejects_minus_one(self):
        with self.assertRaises(ValueError):
            circle_area(-1)


    def test_circle_circumference_rejects_minus_one(self):
        with self.assertRaises(ValueError):
            circumference(-1)


    def test_square_area_rejects_minus_one(self):
        with self.assertRaises(ValueError):
            square_area(-1)


    def test_square_perimeter_rejects_minus_one(self):
        with self.assertRaises(ValueError):
            perimeter(-1)


    def test_circle_area_rejects_negative_fraction(self):
        with self.assertRaises(ValueError):
            circle_area(-0.5)


    def test_circle_circumference_rejects_negative_fraction(self):
        with self.assertRaises(ValueError):
            circumference(-0.5)


    def test_square_area_rejects_negative_fraction(self):
        with self.assertRaises(ValueError):
            square_area(-0.5)


    def test_square_perimeter_rejects_negative_fraction(self):
        with self.assertRaises(ValueError):
            perimeter(-0.5)


    def test_circle_area_rejects_negative_float(self):
        with self.assertRaises(ValueError):
            circle_area(-10.0)


    def test_circle_circumference_rejects_negative_float(self):
        with self.assertRaises(ValueError):
            circumference(-10.0)


    def test_square_area_rejects_negative_float(self):
        with self.assertRaises(ValueError):
            square_area(-10.0)


    def test_square_perimeter_rejects_negative_float(self):
        with self.assertRaises(ValueError):
            perimeter(-10.0)


    def test_circle_area_rejects_nan(self):
        with self.assertRaises(ValueError):
            circle_area(float('nan'))


    def test_circle_circumference_rejects_nan(self):
        with self.assertRaises(ValueError):
            circumference(float('nan'))


    def test_square_area_rejects_nan(self):
        with self.assertRaises(ValueError):
            square_area(float('nan'))


    def test_square_perimeter_rejects_nan(self):
        with self.assertRaises(ValueError):
            perimeter(float('nan'))


    def test_circle_area_rejects_positive_infinity(self):
        with self.assertRaises(ValueError):
            circle_area(float('inf'))


    def test_circle_circumference_rejects_positive_infinity(self):
        with self.assertRaises(ValueError):
            circumference(float('inf'))


    def test_square_area_rejects_positive_infinity(self):
        with self.assertRaises(ValueError):
            square_area(float('inf'))


    def test_square_perimeter_rejects_positive_infinity(self):
        with self.assertRaises(ValueError):
            perimeter(float('inf'))


    def test_circle_area_rejects_negative_infinity(self):
        with self.assertRaises(ValueError):
            circle_area(float('-inf'))


    def test_circle_circumference_rejects_negative_infinity(self):
        with self.assertRaises(ValueError):
            circumference(float('-inf'))


    def test_square_area_rejects_negative_infinity(self):
        with self.assertRaises(ValueError):
            square_area(float('-inf'))


    def test_square_perimeter_rejects_negative_infinity(self):
        with self.assertRaises(ValueError):
            perimeter(float('-inf'))



if __name__ == "__main__":
    unittest.main(verbosity=2)
