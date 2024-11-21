import unittest
from geometric_lib import circle, rectangle, square, triangle
from geometric_lib import trapezoid, rhombus, parallelogram, ellipse


class TestGeometricLib(unittest.TestCase):

    def test_circle(self):
        self.assertAlmostEqual(circle.area(5), 78.53981633974483)
        self.assertAlmostEqual(circle.perimeter(5), 31.41592653589793)
        self.assertAlmostEqual(circle.area(1), 3.141592653589793)
        self.assertAlmostEqual(circle.area(10), 314.1592653589793)
        self.assertAlmostEqual(circle.perimeter(10), 62.83185307179586)

    def test_rectangle(self):
        self.assertEqual(rectangle.area(4, 6), 24)
        self.assertEqual(rectangle.perimeter(4, 6), 20)
        self.assertEqual(rectangle.area(2, 5), 10)
        self.assertEqual(rectangle.area(3, 7), 21)
        self.assertEqual(rectangle.perimeter(3, 7), 20)

    def test_square(self):
        self.assertEqual(square.area(3), 9)
        self.assertEqual(square.perimeter(3), 12)
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(7), 49)
        self.assertEqual(square.perimeter(7), 28)

    def test_triangle(self):
        self.assertEqual(triangle.area(4, 3), 6)
        self.assertEqual(triangle.perimeter(4, 5, 6), 15)
        self.assertEqual(triangle.area(10, 5), 25)
        self.assertEqual(triangle.area(6, 8), 24)
        self.assertEqual(triangle.perimeter(5, 12, 13), 30)

    def test_trapezoid(self):
        self.assertEqual(trapezoid.area(5, 7, 4), 24)
        self.assertEqual(trapezoid.perimeter(5, 7, 6, 8), 26)
        self.assertEqual(trapezoid.area(3, 5, 4), 16)
        self.assertEqual(trapezoid.perimeter(3, 5, 4, 6), 18)

    def test_rhombus(self):
        self.assertEqual(rhombus.area(10, 6), 30)
        self.assertEqual(rhombus.perimeter(5), 20)
        self.assertEqual(rhombus.area(8, 4), 16)
        self.assertEqual(rhombus.perimeter(7), 28)

    def test_parallelogram(self):
        self.assertEqual(parallelogram.area(8, 4), 32)
        self.assertEqual(parallelogram.perimeter(5, 6), 22)
        self.assertEqual(parallelogram.area(10, 5), 50)
        self.assertEqual(parallelogram.perimeter(3, 7), 20)

    def test_ellipse(self):
        self.assertAlmostEqual(ellipse.area(5, 3), 47.12388980384689)
        self.assertAlmostEqual(ellipse.perimeter(5, 3), 25.526986393758545)
        self.assertAlmostEqual(ellipse.area(10, 4), 125.66370614359172)
        self.assertAlmostEqual(ellipse.perimeter(10, 4), 46.02562463041513)

if __name__ == '__main__':
    unittest.main()