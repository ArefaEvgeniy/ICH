# name = input('Enter your name: ')
# balance = input('Enter your balance: ')

name = 'Adam'
balance = 1234.56

string = "Hello, {}, your balance is {}. Byu, {}".format(name, balance, name)
string_2 = "Hello, {0}, your balance is {1}. Byu {4}, {0}".format(name, balance, '123', 222, '5555')
string_3 = ("Hello, {name}, your balance is {balance}. Byu, {new_name}"
            .format(name=name, balance=balance, new_name=name+'!'))


print(string)
print(string_3)

print("Hello {0}, your balance is {blc}.".format(name, blc=230.2346))
