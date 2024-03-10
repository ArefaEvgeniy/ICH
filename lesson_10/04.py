import math
from math import cos

a = 16

print(a ** 0.5)
print(math.sqrt(a))
print(cos(15))
print(math.log(a))
print(math.sin(math.pi / 2))

# e ** 25

print(math.e ** 25)
print(math.exp(25))

x = 2
y_1 = x ** x ** x ** x
y_2 = math.pow(x, math.pow(x, math.pow(x, x)))

print(y_1)
print(y_2)

print(math.ceil(5.5))
print(math.floor(5.5))
print(round(5.5))

print(math.radians(15))
print(math.degrees(0.2617993877991494))

print(math.factorial(5))
