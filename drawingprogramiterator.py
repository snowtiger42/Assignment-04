from shape import Shape

class DrawingProgramIterator:

    def __init__(self, shapesList=None):
        if shapesList is None:
            shapesList = [Shape]
        else:
            self.__shapes = shapesList
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__shapes):
            raise StopIteration()
        shape = self.__shapes[self.__index]
        self.__index += 1
        return shape

    def __iter__(self):
        return self

