def my_func(b, d, c=99):
    print('b:', b)
    print('d:', d)
    print('c:', c)
    a = b + d + c
    return a


a = 10
b = 5
c = 0
value_1 = my_func(a, c)
print(value_1)
value_2 = my_func(a, c=b, d=11)
print(value_2)
