def func(a, b, *args):
    print(a)
    print(b)
    print(args)
    return a + b


func(1, 2)
# lambda a, b, *args: [i*2 for i in args if i > 0]

