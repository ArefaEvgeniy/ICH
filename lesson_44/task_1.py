# Создать класс Car (машина) со следующими полями: model, year, color.
# Создать 10 объектов этого класса, описывающих модели разных марок,
# лет и цветов.
# Создать список из этих объектов.
# Написать функцию, которая принимает список объектов класса Car и цвет и
# возвращает список машин этого цвета. Напечатать этот список, выводя название
# модели, год и цвет. Использовать filter и lambda функции.


class Car:
    def __init__(self, model, year, color='black'):
        self.model = model
        self.year = year
        self.color = color


def filter_car(cars, color):
    for car in filter(lambda car: car.color == color, cars):
        print(f"Модель: {car.model}, Год: {car.year}, Цвет: {car.color}")


car1 = Car("BMW M5", 2023, "blue")
car2 = Car("BMW M1", 2023, "white")
car3 = Car("BMW M3", 2009)
car4 = Car("BMW M5 F90", 2011, "red")
car5 = Car("BMW M7", 2022, "black")
car6 = Car("BMW M4", 2021, "gray")
car7 = Car("BMW M4 Com", 2020, "pink")
car8 = Car("BMW M2", 2024, "red")
car9 = Car("Volvo XS", 2017, "green")
car10 = Car("BMW M5", 2012, "elow")
cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]


filter_car(cars, 'green')
