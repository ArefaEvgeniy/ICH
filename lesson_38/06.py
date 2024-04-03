from itertools import zip_longest

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2]
symbols = ('$', '^', '&')

zipped_1 = list(zip_longest(letters, numbers, symbols, fillvalue='-'))
zipped_2 = list(zip(letters, numbers, symbols))

print(zipped_1)
print(zipped_2)
