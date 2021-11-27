from shape import Shape

"""
Child class triangle has the attributes name, base, height, length1, length2 and length3 which will be utilized in my 
methods. Attribute 'name' is used to determine the name of this classes shape (here it will be 'Triangle'). An exception
is activated if the name is not 'Triangle'. Attribute 'base, height, length1, length2, length3' is used specifically for
the perimeter and area methods. Perimeter takes the inputted length1, length2 and length3 and adds them to each other 
(self.__length1 + self.__length2 + self.__length3). Area takes the inputted base and height and multiplies them to each 
other; then divides them by 2 ((self.__base * self.__height) / 2). The draw methods calls the __str__ method which 
prints out the inputted name and the results of the area and perimeter methods.

"""

class Triangle(Shape):
    def __init__(self, name, base, height, length1, length2, length3):
        super().__init__(name)
        self.__name = name
        self.__base = base
        self.__height = height
        self.__length1 = length1
        self.__length2 = length2
        self.__length3 = length3

        if self.__name != "Triangle":
            raise Exception("Wrong Name or data type")

        if self.__length1 <= 0 or self.__length2 <= 0 or self.__length3 <= 0:
            raise ValueError("None of the lengths can be negative! That make's the Perimeter negative!!!")

        if self.__base <= 0 or self.__height <= 0:
            raise ValueError("Neither the height or base can be negative! That make's the Area negative!!!")

    def get_name(self):
        return self.__name

    def perimeter(self):
        return self.__length1 + self.__length2 + self.__length3

    def area(self):
        return (self.__base * self.__height) / 2

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

