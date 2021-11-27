from shape_factory import ShapeFactory
from DrawingProgram import DrawingProgram


class DrawingProgramMain:
    def __init__(self):
          drawing_program = DrawingProgram()
        # drawing_program.add_shape(ShapeFactory.create_circle(-2.0))
        # drawing_program.add_shape(ShapeFactory.create_rectangle(5.0, 4.0))
        # drawing_program.add_shape(ShapeFactory.create_triangle(3.0))
        # drawing_program.add_shape(ShapeFactory.create_triangle(9.0))
        # drawing_program.add_shape(ShapeFactory.create_square(6.0))
        # drawing_program.add_shape(ShapeFactory.create_rectangle(3.0, 4.0))
        # print(drawing_program)
        # drawing_program.remove_shape(ShapeFactory.create_rectangle(5.0, 4.0))
          print(drawing_program)
        # drawing_program.print_shape(ShapeFactory.create_rectangle(5.0, 4.0))
        # print(drawing_program.get_shape(-6))
        # print(drawing_program.get_shape(5))
        # print(drawing_program.get_shape(0))
        # print(drawing_program.get_shape(7))
        # drawing_program.set_shape(0, ShapeFactory.create_rectangle(5.0, 4.0))
        # drawing_program.sort_shapes()
        # print(drawing_program)
        # drawing_program.set_shape(0, ShapeFactory.create_rectangle(20.0, 4.0))
        # print(drawing_program)
        # drawing_program.sort_shapes()
        # print(drawing_program)

    print("Printing for loop:")
    drawing_program = DrawingProgram()
    for shape in drawing_program:
        print(shape)


if __name__ == "__main__":
    dp = DrawingProgramMain()