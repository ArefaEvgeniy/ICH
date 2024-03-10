import decimal


decimal.getcontext().prec = 35
number1 = decimal.Decimal('1')
number2 = decimal.Decimal('7')
result = number1 / number2
print(result)

num_1 = 1
num_2 = 7
res = num_1 / num_2
print(res)
