import itertools
import operator
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
result = itertools.accumulate(numbers, operator.mul)
print(list(result))
# Результат: [1, 2, 6, 24, 120]

result_2 = reduce(operator.mul, numbers)
print(result_2)
