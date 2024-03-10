import decimal


decimal.getcontext().prec = 20
number1 = decimal.Decimal('0.1')
number2 = decimal.Decimal('0.2')
result = number1 + number2
print(result)  # Выводит: 0.3

num_1 = 0.1
num_2 = 0.2
res = num_1 + num_2
print(res)
