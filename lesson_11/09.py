a_1 = 10
a_2 = 10

print(id(a_1))
print(id(a_2))

str_1 = 'Hello, world!'
str_2 = 'Hello, world!'

print(id(str_1))
print(id(str_2))

a = str_1[1:5]
print(a)
print(str_1)

b = str_1[:]
print(b)
print(id(b))
