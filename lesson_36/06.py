numbers = [1, 2]
letters = ['a', 'b', 'c', 'd']
zipped = zip(numbers, letters)
print(list(zipped))
print(next(zipped))
print(next(zipped))

# for num, letter in zipped:
#     print(num, letter)
