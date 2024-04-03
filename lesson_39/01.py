# class Dog:
# class Dog():
class Dog(object):
    number_of_foot = 4
    tail = True
    color = 'white'

    def say(self):
        print('Wof, wof')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step {item}', end=', ')
        print()


dog_1 = Dog()
dog_1.say()
print(dog_1.color)
dog_1.go()

print('-' * 50)

dog_2 = Dog()
dog_2.say()
dog_2.number_of_foot = 3
dog_2.name = 'Jessy'
print(dog_1.number_of_foot)
print(dog_2.number_of_foot)
dog_2.go()

Dog.number_of_foot = 5

print(dog_1.__dict__)
print(dog_2.__dict__)
print(dog_1.number_of_foot)
print(dog_2.number_of_foot)
print(Dog.number_of_foot)

# print(dir(Dog))
