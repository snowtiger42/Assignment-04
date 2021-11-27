from math import pi
from shape import Shape

"""
Child class circle has the attributes name and radius which will be utilized in my methods. Attribute 'name' is used to 
determine the name of this classes shape (here it will be 'Circle'). An exception is activated if the name is not 
'Circle'. Attribute 'radius' is used specifically for the perimeter and area methods. Perimeter takes the inputted 
radius and multiplies it by pi. Then it multiples again by 2 (2 * (pi * self.__radius)). Area takes the inputted 
radius and squares itself, then multiplies it by pi (pi * (self.__radius ** 2)). The draw methods calls the __str__ 
method which prints out the inputted name and the results of the area and perimeter methods.

"""


class Circle(Shape):

    def __init__(self, name, radius):
        super().__init__(name)
        self.__name = name
        self.__radius = radius

        if self.__name != "Circle":
            raise Exception("Wrong Name or data type")
        if self.__radius <= 0:
            raise ValueError("The radius cannot be negative! That make's the Perimeter negative!!!")

    def get_name(self):
        return self.__name

    def perimeter(self):
        return 2 * (pi * self.__radius)

    def area(self):
        return pi * (self.__radius ** 2)

    def draw(self):
        return self.__str__()

    def __str__(self):
        return self.get_name() + ": Area = "+ str(self.area()) + " Perimeter = " + str(self.perimeter())

    def __le__(self, other: Shape):
        if self.get_name() < other.get_name():
            return True
        elif self.get_name() == other.get_name() and self.area() < other.area():
            return True
        return False

