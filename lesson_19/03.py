a = [1, '3', 22.23, 99, 22.23]
b = [1, '3', 22.23, 99, 22.23]

print(id(a))
print(id(b))

a.remove(99)
print(a)
print(b)
b.append(1001)
print(a)
print(b)
