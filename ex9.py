import math


class Parallelogram():

    ''' A class representing a parallelogram'''

    def __init__(self, base, side, theta):
        '''(Parallelogram, float, float, float) -> Nonetype
        Set up a new parallelogram with length of base, length of side and the
        angle theta
        '''
        self.base = base
        self.side = side
        self.theta = theta

    def area(self):
        ''' (Parallelogram) -> float
        returns the area of the shape
        '''
        # height equals to side * sin(theta)
        height = self.side * math.sin(math.radians(self.theta))
        # area equals to base times height
        area = self.base * height
        return area

    def bst():
        ''' (Parallelogram) -> list of floats
        returns a list of three floats: [base, side, theta]
        '''
        return [base, side, theta]

    def __str__(self):
        '''(Parallelogram) -> str
        Returns a string representing the area of the parallelogram
        '''
        return "I am a " + str(type(self).__name__) + " with area" + \
               " " + str(self.area())


class Rectangle(Parallelogram):
    ''' A class representing a rectangle'''

    def __init__(self, base, side):
        '''(rectangle, float, float, float) -> Nonetype
        Set up a new rectangle with length of base, length of side
        '''
        # a rectangle is just a parallelogram with theta equals to 90
        Parallelogram.__init__(self, base, side, 90)


class Rhombus(Parallelogram):
    '''A class representing a rhombus'''
    def __init__(self, base, theta):
        '''(rhombus, float, float) -> Nonetype
        Set up a new rhombus with length of base, the angle theta
        '''
        # a rhombus is just a parallelogram with the four sides equal
        Parallelogram.__init__(self, base, base, theta)


class Square(Rhombus, Rectangle, Parallelogram):
    '''A class representing a square'''
    def __init__(self, base):
        '''(square, float) -> Nonetype
        Set up a new square with length of base
        '''
        # a square is just a rhombus with theta equal to 90
        Rhombus.__init__(self, base, 90)


if (__name__ == "__main__"):

    A = Parallelogram(100, 2, 90)
    B = Square(2)
    C = Rectangle(2, 3)

    print(A)
    print(B)
    print(C)
