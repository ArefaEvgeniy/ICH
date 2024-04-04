from task_01 import Point


class Circle(Point):

    def __init__(self, x=0, y=0, radius=1, color=None):
        super().__init__(x, y, color)
        self.radius = radius

    def __str__(self):
        return f'Circle(X:{self.x}, Y:{self.y}, radius={self.radius})'


circle = Circle(3, 5)
print(circle)
print(circle.get_color())
