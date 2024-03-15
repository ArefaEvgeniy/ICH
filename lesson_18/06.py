a = [1, '3', 22.23, 99]
b = ['qw', 'ert', 0, -2]

c = a + b

a.extend(b)
print(a)
print(c)

a_1 = ['a', 'b', 'c', 'd']
a_2 = [2, 4, 6, 8]

a_0 = []
for index, value in enumerate(a_1):
    a_0.append(value)
    a_0.append(a_2[index])

print(a_0)
