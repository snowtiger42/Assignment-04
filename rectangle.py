from shape import Shape

"""
Child class rectangle has the attributes name, width and height which will be utilized in my methods. Attribute 'name' 
is used to determine the name of this classes shape (here it will be 'Rectangle'). An exception is activated if the name
is not 'Rectangle'. Attribute 'width and height' is used specifically for the perimeter and area methods. Perimeter 
takes the inputted width and height and then adds them to each other, then multiples them by 2 
(2 * (self.__width + self.__height)). Area takes the inputted width and height and multiplies them by each other 
(self.__width * self.__height). The draw methods calls the __str__ method which prints out the inputted name and the 
results of the area and perimeter methods.

"""

class Rectangle(Shape):

    def __init__(self, name, width, height):
        super().__init__(name)
        self.__name = name
        self.__width = width
        self.__height = height

        if self.__name != "Rectangle":
            raise Exception("Wrong Name or data type")

        if self.__width <= 0 or self.__height < 0:
            raise ValueError("The height and width cannot be negative! That make's the Perimeter negative!!!")

    def get_name(self):
        return self.__name

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def area(self):
        return self.__width * self.__height

    def draw(self):
        return self.__str__()

    def __str__(self):
        return self.get_name() + ": Area = " + str(self.area()) + " Perimeter = " + str(self.perimeter())

    def __le__(self, other: Shape):
        if self.get_name() < other.get_name():
            return True
        elif self.get_name() == other.get_name() and self.area() < other.area():
            return True
        return False

