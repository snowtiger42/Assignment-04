import unittest

from circle import Circle
from shape_factory import ShapeFactory
from square import Square
from rectangle import Rectangle
from triangle import Triangle


class MyShapeFactoryTests(unittest.TestCase):

    def test_square_created(self):
        """Test if square with area side length unit of 2.0 created"""
        sq1 = ShapeFactory.create_square(2.0)
        sq2 = Square('Square', 2.0)
        self.assertEqual(sq1.draw(), sq2.draw())

    def test_circle_created(self):
        """Test if circle with area radius unit of 2.0 created"""
        c1 = ShapeFactory.create_circle(2.0)
        c2 = Circle('Circle', 2.0)
        self.assertEqual(c1.draw(), c2.draw())

    def test_rectangle_created(self):
        """Test if rectangle with area unit of width 2.0 and height 3.0 created"""
        rec1 = ShapeFactory.create_rectangle(2.0, 3.0)
        rec2 = Rectangle('Rectangle', 2.0, 3.0)
        self.assertEqual(rec1.draw(), rec2.draw())

    def test_triangele_created(self):
        """Test if triangle with area unit of base 2.0 and height 3.0 created"""
        tri1 = ShapeFactory.create_triangle(2.0, 3.0, 2.0, 9.0, 10.0)
        tri2 = Triangle('Triangle', 2.0, 3.0, 2.0, 9.0, 10.0)
        self.assertEqual(tri1.draw(), tri2.draw())

    def test_create_circle_negative_radius(self):
        """Creating a circle with negative value(radius) which should raise an exception of type ValueError"""
        try:
            circleneg = ShapeFactory.create_circle(-1)
            self.assertEqual(True, False, "exception not thrown for radius of -1")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_create_rectangle_negative_dimension(self):
        """Creating a rectangle with negative width/height value which should raise an exception of type ValueError"""
        try:
            ShapeFactory.create_rectangle('Rectangle', -1)
            self.assertEqual(True, False, "exception not thrown for radius of -1")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_create_square_negative_width(self):
        """Creating a square with negative side length value which should raise an exception of type ValueError"""
        try:
            ShapeFactory.create_square(-2)
            self.assertEqual(True, False, "exception not thrown for radius of -1")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_create_triangle_negative_width_or_height(self):
        """Creating a circle with negative value(width or/and height)
        which should raise an exception of type ValueError"""
        try:
            ShapeFactory.create_triangle(-1, -2, -3, -4, -5)
            self.assertEqual(True, False, "exception not thrown for radius of -1")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_create_circle_zero_radius(self):
        """Creating a circle with 0 value(radius) which should raise an exception of type ValueError"""
        try:
            ShapeFactory.create_circle(0)
            self.assertEqual(True, False, "exception not thrown for radius of 0")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_create_rectangle_zero_width_or_height(self):
        """Creating a circle with 0 value(width_or_height) which should raise an exception of type ValueError"""
        try:
            ShapeFactory.create_rectangle(0, 0)
            self.assertEqual(True, False, "exception not thrown for width_or/and_height of 0")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_create_square_zero_width(self):
        """Creating a circle with 0 value(side length) which should raise an exception of type ValueError"""
        try:
            ShapeFactory.create_square(0)
            self.assertEqual(True, False, "exception not thrown for width of 0")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_create_triangle_zero_width_or_height(self):
        """Creating a circle with 0 value(width_or_height) which should raise an exception of type ValueError"""
        try:
            ShapeFactory.create_triangle(0, 0, 0, 0, 0)
            self.assertEqual(True, False, "exception not thrown for width_or/and_height of 0")
        except ValueError as value_error:
            self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()