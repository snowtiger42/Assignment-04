import abc

"""
The abstract base class for all four of the child shape classes to inherit from. They must all utilize the methods in
this class in order to inherit (though none of these methods may be instantiated). The area (and perimeter) method will 
enable each child shape to utilize a common method for each. This is useful because while each child shape will have the 
same method, the way each child class will use them will be entirely different and use different attributes. The draw
method will be use to call each shape and display their names, area: (), perimeter: (). This will be done with the help
of the __str__ method.
"""

class Shape(metaclass=abc.ABCMeta):

    def __init__(self, name: str) -> None:
        self._name = name
        self._name = name

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def area(self):
        """
       Calculate the area of the shape.

       Returns:
       (float): the area of the shape.
       """
        pass

    @abc.abstractmethod
    def perimeter(self):
        """
       Calculate the perimeter of the shape.

       Returns:
       (float): the perimeter of the shape.
       """
        pass

    @abc.abstractmethod
    def draw(self):
        return self.__str__()

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def __le__(self, other):
        pass
