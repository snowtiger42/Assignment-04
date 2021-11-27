from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from square import Square
from shape import Shape
"""Docstring"""

class ShapeFactory:
    @staticmethod
    def to_positive_number(num_type, *args):
        """Check if a passed value can be represented as an input number type greater than zero,
        else Raises asn exception and  returns an error message if false"""
        for number in args:
            if num_type(float(number)) > 0:
                yield num_type(float(number))
            else:
                raise ValueError('Value must be convertible to the provided number type and greater than zero')

    @staticmethod
    def create_circle(radius):
        """This method creates a circle based on the radius value passed to the static method."""
        radius, = ShapeFactory.to_positive_number(float, radius)
        return Circle('Circle', radius)

    @staticmethod
    def create_square(side_length):
        """This method creates a square shape based on the width value passed to the static method."""
        width, = ShapeFactory.to_positive_number(float, side_length)
        return Square('Square', width)

    @staticmethod
    def create_rectangle(width, height):
        """This method creates a rectangle shape based on the width and height values passed to the static method."""
        width, = ShapeFactory.to_positive_number(float, width)
        height, = ShapeFactory.to_positive_number(float, height)
        return Rectangle('Rectangle', width, height)

    @staticmethod
    def create_triangle(base, height, length1, length2, length3):
        """This method creates a triangle shape based on the width and height values passed to the static method."""
        base, = ShapeFactory.to_positive_number(float, base)
        height, = ShapeFactory.to_positive_number(float, height)
        length1, = ShapeFactory.to_positive_number(float, length1)
        length2, = ShapeFactory.to_positive_number(float, length2)
        length3, = ShapeFactory.to_positive_number(float, length3)
        return Triangle('Triangle', base, height, length1, length2, length3)
