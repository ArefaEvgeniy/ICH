a = [1, '3', 22.23, 99]

print(a)
print(id(a))
print(type(a))
print(len(a))

print('-' * 50)
a.append(True)
print(a)
print(id(a))
print(type(a))
print(len(a))

print('-' * 50)
a.append([1, 2, 3, 'rrr'])
print(a)
print(id(a))
print(len(a))

print('-' * 50)
a.insert(1, 100.66)
print(a)
print(id(a))
print(len(a))
