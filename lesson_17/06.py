def my_func(b=99, d=70):
    a = b + d
    return a


a = 10
b = 5
c = 0
value_1 = my_func(a, c)
print(value_1)
value_2 = my_func(a)
print(value_2)
value_3 = my_func()
print(value_3)
