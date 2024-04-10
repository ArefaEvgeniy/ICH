class Person:
    def __init__(self, name, surname):
        self.surname = surname
        if name.isalpha():
            self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name.isalpha():
            self.__name = new_name

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, new):
        self.name, self.surname = new.split()

    @fullname.deleter
    def fullname(self):
        pass


obj = Person('Tom', 'Kruz')
print(obj.name)
print(obj.surname)
print(obj.fullname)

obj.surname = 'White'
print('-' * 50)
print(obj.name)
print(obj.surname)
print(obj.fullname)

print('-' * 50)
obj.fullname = 'Bob Red'
print(obj.name)
print(obj.surname)
print(obj.fullname)

obj.name = '1sdg'
print(obj.name)
