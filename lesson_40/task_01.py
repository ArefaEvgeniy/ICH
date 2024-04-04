import math

class Point(object):
    DEFAULT_COLOR = 'black'

    def __init__(self, x=0, y=0, color=DEFAULT_COLOR):
        self.x = x
        self.y = y
        self.__color = self.valid_color(color)

    def __str__(self):
        return f'Point(X:{self.x}, Y:{self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y}, "{self.__color}")'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        color = self.__color
        return Point(x, y, color)

    def valid_color(self, color):
        return color if isinstance(color, str) and color else Point.DEFAULT_COLOR

    def get_color(self):
        return f'{self.__class__.__name__} is {self.__color}'

    def distance_from_origin(self):
        return round(math.hypot(self.x, self.y), 2)


if __name__ == "__main__":
    point_01 = Point()
    point_02 = Point(10, 4, 'red')
    point_03 = Point(y=10, color=55)

    print(point_02.get_color())
    print(point_02.x)
    print(point_02.distance_from_origin())

    print(point_03.__dict__)
    print(point_03.DEFAULT_COLOR)

    print(point_03)

    print(repr(point_03))

    point_04 = Point(0, 10, "black")
    print(point_04.__dict__)

    point_05 = point_02 + point_03
    print(point_05)
    print(point_05.get_color())
