from DrawingProgram import DrawingProgram
from shape_factory import ShapeFactory
from circle import Circle
from square import Square
from rectangle import Rectangle
from triangle import Triangle


class DrawingProgramMain:
    circle = Circle("Circle", 1.0)
    square = Square("Square", 1.0)
    rectangle = Rectangle("Rectangle", 1.0, 1.0)
    triangle = Triangle("Triangle", 1.0, 1.0, 1.0, 1.0, 1.0)

    drawing_program = DrawingProgram()

    drawing_program.add_shape(ShapeFactory.create_square(4.0))
    drawing_program.add_shape(ShapeFactory.create_circle(7.0))
    drawing_program.add_shape(ShapeFactory.create_circle(1.0))
    drawing_program.add_shape(ShapeFactory.create_rectangle(3.0, 6.0))
    drawing_program.add_shape(ShapeFactory.create_triangle(3.0, 2.0, 3.0, 4.0, 5.0))
    drawing_program.add_shape(ShapeFactory.create_square(2.0))
    drawing_program.add_shape(ShapeFactory.create_rectangle(2.0, 4.0))
    drawing_program.add_shape(ShapeFactory.create_triangle(1.0, 9.0, 7.0, 4.0, 6.0))

    print("---------Print--------------")
    drawing_program.print_shape(triangle)
    drawing_program.print_shape(rectangle)
    drawing_program.print_shape(square)
    drawing_program.print_shape(circle)

    print("\n\n---------String Shapes--------------")
    print(drawing_program.__str__())

    print("\n\n---------Sort Shapes--------------")
    drawing_program.sort_shapes()
    print(drawing_program.__str__())

    print("\n\n---------Get Shapes--------------")

    shape = drawing_program.get_shape(3)
    print(shape.draw())

    print("\n\n---------Set Shapes--------------")

    drawing_program.set_shape()

    print("\n\n---------Delete Circle--------------")
    drawing_program.remove_shape(circle)
    drawing_program.remove_shape(circle)
    print(drawing_program.__str__())
    # drawing_program.print_shape(triangle)
    # drawing_program.print_shape(rectangle)
    # drawing_program.print_shape(square)
    # drawing_program.print_shape(circle)

    pass
