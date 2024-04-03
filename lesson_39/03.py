class Dog(object):
    number_of_foot = 4
    tail = True
    color = 'white'

    def __init__(self, tail=True, color='white', number_of_foot=4):
        self.tail = tail
        self.color = color
        self.number_of_foot = number_of_foot

    def say(self):
        print('Wof, wof')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step {item}', end=', ')
        print()


dog_1 = Dog(True, 'Black', 4)
# dog_1.tail = True
# dog_1.color = 'Black'
# dog_1.number_of_foot = 4

dog_2 = Dog(False)
# dog_2.tail = True
# dog_2.color = 'white'
# dog_2.number_of_foot = 3

dog_3 = Dog(number_of_foot=3)

Dog.number_of_foot = 5

print(dog_1.__dict__)
print(dog_2.__dict__)
print(dog_3.__dict__)
