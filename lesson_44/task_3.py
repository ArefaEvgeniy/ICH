# Создать класс Shape, описывающий абстрактную фигуру, у которой есть площадь.
# У этого класса есть метод calculateArea(), который возвращает площадь фигуры.
# У класса также есть поле name, которое содержит строчное название фигуры.
# Например, “круг”, “прямоугольник” и так далее.
# Унаследовать от класса Shape 3 других класса: Circle, Square, Rectangle.
# У каждого класса должны быть соответствующие поля и конструкторы, а также
# определены функции печати этих полей. Для каждого класса переопределить метод
# calculateArea(), который вычисляет площадь фигуры. Создать по два объекта
# каждой фигуры. Составить список с этими объектами и напечатайте площадь каждой
# фигуры, вызывая метод calculateArea().

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def calculateArea(self):
        return None


class Circle(Shape):
    def __init__(self,radius, name):
        self.radius = radius
        super().__init__(name)

    def calculateArea(self):
        return 2 * pi * self.radius ** 2


class Square(Shape):
    def __init__(self, a, name):
        self.a = a
        super().__init__(name)

    def calculateArea(self):
        return self.a ** 2


class Rectangle(Shape):
    def __init__(self, a, b, name):
        self.a = a
        self.b = b
        super().__init__(name)

    def calculateArea(self):
        return self.a * self.b


object1 = Circle(10, 'Circle')
object2 = Square(10, 'Square')
object3 = Rectangle(10, 12, 'Rectangle')


for item in (object1, object2, object3):
    print(f'Площадь {item.calculateArea()}, Название: {item.name}')
