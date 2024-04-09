# Создать класс Person с полями имя и дата рождения.
# Создать 10 объектов этого класса с разными именами.
# Создать класс Employee который содержит поле имя и возраст.
# Написать функцию, которая из списка объектаъов класса Person создает список
# из объектов класса Employee, вычисляя возраст каждого Person по дате
# рождения. Подумать, где должна быть реализована функция, вычисляющая возраст
# по дате рождения. Получившийся список должен содержать сотрудников,
# старше 18 лет. Вывести получившихся сотрудников на экран.

from datetime import date


class Person:

    def __init__(self, name, birth_date):
        birth_date = list(map(int, birth_date.split(".")))
        self.name = name
        self.birth_date = date(birth_date[0], birth_date[1], birth_date[2])

    def get_age(self):
        return date.today().year - self.birth_date.year - (date.today().month < self.birth_date.month)


class Employee:

    def __init__(self, person: Person):
        self.name = person.name
        self.age = person.get_age()

    def __str__(self):
        return f"Name: {self.name} and age: {self.age}"


p_1 = Person("Jack", "2000.12.09")
p_2 = Person("Sam", "2013.06.01")
p_3 = Person("Max", "2015.03.05")
p_4 = Person("Juli", "1984.03.05")
p_5 = Person("Orest", "2020.03.05")
p_6 = Person("Mila", "1600.03.05")

person_list = [p_1, p_2, p_3, p_4, p_5, p_6]
# emp_list = list(filter(lambda emp: emp.age > 18, [Employee(per) for per in person_list]))
emp_list = [Employee(per) for per in person_list if per.get_age() > 18]

for emp in emp_list:
    print(emp)