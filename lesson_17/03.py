def say_hi(name):
    print('Hello', name, '!')
    while True:
        age = input('Enter your age: ')
        if age.isdigit():
            break
        else:
            print('Repeat your age')
    age = int(age)
    return age


name = 'Evgeniy'
...
# print('Hello', name, '!')
my_age = say_hi(name)
...
# print('Hello Dima!')
dima_age = say_hi('Dima')
...
my_name = 'Victoria'
# print('Hello', my_name, '!')
new_age = say_hi(my_name)

print(my_age)
print(dima_age)
print(new_age)
