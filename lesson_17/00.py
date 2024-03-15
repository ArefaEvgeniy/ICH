def my_func(b, d):   # b = ab00023390   -> 0  (0 , 10)  b = 0, d = 10
    a = b + d + 55   # a = 0 + 10 + 55 = 65
    return a


a = 10
b = 5
c = 0
value = my_func(c, a)  # ab00023390  -> 0  (0 , 10)  value = 65
print(value)
