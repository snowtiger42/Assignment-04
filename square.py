from shape import Shape

"""
Child class square has the attributes name and side_length which will be utilized in my methods. Attribute 'name' is 
used to determine the name of this classes shape (here it will be 'Square'). An exception is activated if the name is 
not 'Square'. Attribute 'side_length' is used specifically for the perimeter and area methods. Perimeter takes the 
inputted side_length and multiplies it by four (4 * self.__side_length)). Area takes the inputted side_length and 
squares itself ((self.__radius ** 2)). The draw methods calls the __str__ method which prints out the inputted name and 
the results of the area and perimeter methods.

"""

class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.__name = name
        self.__side_length = side_length

        if self.__name != "Square":
            raise Exception("Wrong Name or data type")

        if self.__side_length <= 0:
            raise ValueError("The side length cannot be negative! That make's the Perimeter negative!!!")

    def get_name(self):
        return self.__name

    def perimeter(self):
        return 4 * self.__side_length

    def area(self):
        return self.__side_length * self.__side_length

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

