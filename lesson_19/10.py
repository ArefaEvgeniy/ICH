# a = 10
# b = 20
# c = 0

a, b, c = 10, 20, 0

# a = b = c = 10

a, c = c, a

print(a)
print(b)
print(c)

d = [1, 2, 3]

print(d)
print(*d)

# a, b, c, e = d
# a, b = d
# a, b, c = d
# a, b, c = 'asdf'
a, b, c = 'asd'

print(a)
print(b)
print(c)
# print(e)

print('-' * 50)
d = (1, 2, 3, 5, 6, 7)
a, b, c, *e = d

print(a)
print(b)
print(c)
print(e)

print('-' * 50)
d = (1, 2, 3, 5)
a, b, c, *e = d

print(a)
print(b)
print(c)
print(e)

print('-' * 50)
d = (1, 2, 3)
a, b, c, *e = d

print(a)
print(b)
print(c)
print(e)
