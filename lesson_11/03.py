a = 1
b = 2.0
c = '3'

print(a + b)
print(type(a + b))

print(a + int(c))
print(str(a) + c)

print(str(int(str(a) + c) + b) + '!')
