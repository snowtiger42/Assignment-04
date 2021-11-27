from drawingprogramiterator import DrawingProgramIterator


class DrawingProgram:
    __shapes = []

    def __init__(self, shapes=None):
        if shapes is not None:
            self.__shapes = shapes

    def add_shape(self, shape):
        self.__shapes.append(shape)

    def remove_shape(self, shape):
        count = 0
        for current_shape in self.__shapes:
            if current_shape.get_name() == shape.get_name():
                self.__shapes.remove(current_shape)
                count += 1
        print("You have deleted ", count, " shapes")
        return count

    def print_shape(self, shape):
        for current_shape in self.__shapes:
            if current_shape.get_name() == shape.get_name():
                print(current_shape.draw())

    def sort_shapes(self):
        self.mergesort(self.__shapes)

    ''' this is my implementation of merge sort for shapes '''

    @staticmethod
    def mergesort(shapes):
        if len(shapes) > 1:
            mid = len(shapes) // 2
            left = shapes[:mid]
            right = shapes[mid:]

            DrawingProgram.mergesort(left)
            DrawingProgram.mergesort(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    shapes[k] = left[i]
                    i += 1
                else:
                    shapes[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                shapes[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                shapes[k] = right[j]
                j += 1
                k += 1

    def __str__(self):
        s = ""
        for shape in self.__shapes:
            s += f"{str(shape)} \n"
        return s

    def get_shape(self, index):
        if index >= 0 and index < len(self.__shapes):
            return self.__shapes[index]
        return None

    def set_shape(self, index, Shape):
        if index >= 0 and index < len(self.__shapes):
            self.__shapes[index] = Shape

    def __iter__(self):
        return DrawingProgramIterator(self.__shapes)
