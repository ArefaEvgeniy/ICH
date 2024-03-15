import copy

a = [1, '3', 22.23, 99, 22.23]
b = a[:]
c = copy.copy(a)
d = list(a)
e = a.copy()

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))

a.remove(99)
print(a)
print(b)
b.append(1001)
print(a)
print(b)