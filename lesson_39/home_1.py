# Создайте класс Rectangle для представления прямоугольника. Класс должен
# иметь атрибуты width (ширина) и height (высота), а также метод
# calculate_area(), который вычисляет площадь прямоугольника. Затем создайте
# экземпляр класса Rectangle с заданными значениями ширины и высоты и
# выведите его площадь.

class Rectangle:
    def __init__(self, height, width):
        self.hight = height
        self.width = width

    def calculate_area(self):
        return self.hight * self.width


ABCD = Rectangle(10, 20)
print("Площадь прямоугольника ABCD:", ABCD.calculate_area())
