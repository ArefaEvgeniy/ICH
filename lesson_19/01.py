a = [1, '3', 22.23, 99, 22.23]
b = a

print(a)
a.remove(22.23)
print(a)

del a[1]
print(a)

del a
print(b)
del b

