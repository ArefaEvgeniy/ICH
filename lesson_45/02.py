class Car:
    NUMBER_OF_CARS = 0
    MES = ''

    def __init__(self, mark, color, year):
        self.mark = mark
        self.color = color
        self.year = year
        Car.NUMBER_OF_CARS += 1
        self.number = Car.NUMBER_OF_CARS

    @classmethod
    def get_number(cls):
        print(f'General objects is {cls.NUMBER_OF_CARS}')

    def get_mes(self, mes):
        Car.MES = mes


class Track(Car):
    NUMBER_OF_CARS = 0

    def __init__(self, mark, color, year):
        self.mark = mark
        self.color = color
        self.year = year
        Track.NUMBER_OF_CARS += 1
        self.number = Track.NUMBER_OF_CARS


car_1 = Car('BMW', 'black', 2020)
car_2 = Car('Lada', 'white', 2000)
car_3 = Car('Zaz', 'fred', 1970)

print(Car.NUMBER_OF_CARS)
print(car_2.NUMBER_OF_CARS)
car_2.get_number()

car_1.get_mes('Car_1 is black')
print(car_3.MES)

track_1 = Track('Volvo V-50', 'black', 2020)
track_2 = Track('Volvo V-50', 'black', 2021)
track_3 = Track('Volvo V-50', 'black', 2020)
track_4 = Track('Volvo V-50', 'black', 2020)

car_1.get_number()
track_1.get_number()

print(Car.NUMBER_OF_CARS)
print(Track.NUMBER_OF_CARS)

Car.get_number()
Track.get_number()
