a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd']
c = ['AA', 'BB', 55]

for item in zip(a, b):
    print(item)

print(list(zip(a, b, c)))
