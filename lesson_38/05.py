import itertools

letters = ['a', 'b', 'c']
numbers = [1, 2]
combinations = list(itertools.combinations(letters, 2))
# Результат: [('a', 'b'), ('a', 'c'), ('b', 'c')]
permutations = list(itertools.permutations(numbers))
# Результат: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
product = list(itertools.product(letters, numbers))
print(product)
# Результат: [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
