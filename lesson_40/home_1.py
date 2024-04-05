# Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями
# по умолчанию, а также методы calculate_area() для вычисления площади
# прямоугольника и calculate_perimeter() для вычисления периметра прямоугольника.
# Переопределить методы __str__, __repr__. Затем создайте экземпляр класса
# Rectangle и выведите информацию о нем, его площадь и периметр.

class Rectangle:
    def __init__(self, hight=0, width=0):
        self.hight = hight
        self.width = width

    def calculate_area(self):
        return self.hight * self.width

    def calculate_perimeter(self):
        return (self.hight + self.width) * 2

    def __str__(self):
        return f'Прямоугольник со сторонами {self.hight} и {self.width}'

    def __repr__(self):
        return f'Rectangle(height={self.hight!r}, width={self.width!r})'


ABCD = Rectangle(10, 20)
print(ABCD)
print("Площадь прямоугольника ABCD:", ABCD.calculate_area())
print("Периметр прямоугольника ABCD:", ABCD.calculate_perimeter())
print(f"Создание прямоугольника: {ABCD!r}")
