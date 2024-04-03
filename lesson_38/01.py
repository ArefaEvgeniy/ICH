a = [1, 2, 3, 4, 5]
b = ('a', 'b', 'c')
c = {0, 5, 7, 3, 1, 4}
d = {5: 'rt', 7: '223', 0: '3', 99: '67'}

print(list(zip(a, b, c)))

print(sorted(a))
print(sorted(b))
print(sorted(c))
print(sorted(d))
print(sorted(d.values()))
