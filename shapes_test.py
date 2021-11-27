import unittest
from circle import Circle
from square import Square
from rectangle import Rectangle
from triangle import Triangle


class TestShapes(unittest.TestCase):
    def test_Circle_Name(self):
        circleName = Circle("Circle", 2)
        self.assertEqual(circleName.get_name(), "Circle")

    def test_Circle_Name_Fail(self):
        circleNameFail = Circle("Circle", 2)
        self.assertNotEqual(circleNameFail.get_name(), "Circleee", "The name of the shape is not 'Circle'!!!")

    def test_Circle_Perimeter(self):
        c3 = Circle("Circle", 2)
        self.assertEqual(c3.perimeter(), 12.566370614359172)

    def test_Negative_Circle_Perimeter(self):
        try:
            cNep0 = Circle("Circle", -1)
            self.assertEqual(True, False)
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_Circle_Area(self):
        circle1 = Circle("Circle", 1.0)
        circle2 = Circle("Circle", 2.0)

        self.assertAlmostEqual(circle1.area(), 3.141592653589793)
        self.assertAlmostEqual(circle2.area(), 12.566370614359172)

    def test_Negative_Circle_Area(self):
        try:
            circleNeg = Circle("Circle", -2.0)
            self.assertEqual(True, False)
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_Square_Name(self):
        squareName = Square("Square", 2)
        self.assertEqual(squareName.get_name(), "Square")

    def test_Square_Name_Fail(self):
        squareNameFail = Square("Square", 2)
        self.assertNotEqual(squareNameFail.get_name(), "Squareee", "The name of the shape is not 'Square'!!!")

    def test_Square_Perimeter(self):
        s0 = Square("Square", 2.5)
        self.assertEqual(s0.area(), 6.25)

    def test_Negative_Square_Perimeter(self):
        try:
            sNeg = Square("Square", -2.5)
            self.assertEqual(True, False)
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_Square_Area(self):
        s1 = Square("Square", 2.5)
        self.assertEqual(s1.area(), 6.25)

    def test_Negative_Square_Area(self):
        try:
            sNeg2 = Square("Square", -2.5)
            self.assertEqual(True, False)
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_Rectangle_Name(self):
        rectangleName = Rectangle("Rectangle", 2.5, 5)
        self.assertEqual(rectangleName.get_name(), "Rectangle")

    def test_Rectangle_Name_Fail(self):
        rectangleNameFail = Rectangle("Rectangle", 2.5, 5)
        self.assertNotEqual(rectangleNameFail.get_name(), "Rectangleee", "The name of the shape is not 'Rectangle'!!!")

    def test_Rectangle_Perimeter(self):
        r1 = Rectangle("Rectangle", 2.5, 5)
        self.assertEqual(r1.perimeter(), 15)

    def test_Negative_Rectangle_Perimeter(self):
        try:
            rNeg1 = Rectangle("Rectangle", -2.5, 5)
            self.assertEqual(True, True, False)
        except ValueError as value_error:
            self.assertEqual(True, True, True)

    def test_Rectangle_Area(self):
        r2 = Rectangle("Rectangle", 2.5, 5)
        self.assertEqual(r2.area(), 12.5)

    def test_Negative_Rectangle_Area(self):
        try:
            rNeg2 = Rectangle("Rectangle", -2.5, 5)
            self.assertEqual(True, True, False)
        except ValueError as value_error:
            self.assertEqual(True, True, True)

    def test_Triangle_Name(self):
        triangleName = Triangle("Triangle", 5, 4, 3, 2, 1)
        self.assertEqual(triangleName.get_name(), "Triangle")

    def test_Triangle_Name_Fail(self):
        triangleNameFail = Triangle("Triangle", 5, 4, 3, 2, 1)
        self.assertNotEqual(triangleNameFail.get_name(), "Triangleee", "The name of the shape is not 'Rectangle'!!!")

    def test_Triangle_Perimeter(self):
        t0 = Triangle("Triangle", 5, 4, 3, 2, 1)
        self.assertEqual(t0.perimeter(), 6)

    def test_Negative_Triangle_Perimeter(self):
        try:
            tNeg1 = Triangle("Triangle", 5, 4, -2, 3, 1)
            self.assertEqual(True, True, False)
        except ValueError as value_error:
            self.assertEqual(True, True, True)

    def test_Triangle_Area(self):
        t1 = Triangle("Triangle", 3.3, 2.1, 3, 5, 2.5)
        self.assertEqual(t1.area(), 3.465)

    def test_Negative_Triangle_Area(self):
        try:
            tNeg2 = Triangle("Triangle", 5, 4, -2, 3, 1)
            self.assertEqual(True, True, False)
        except ValueError as value_error:
            self.assertEqual(True, True, True)


if __name__ == '__main__':
    unittest.main()
