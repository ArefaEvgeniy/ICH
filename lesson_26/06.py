def func_1(*args):
    print(args)


func_1(12, 3, 5, 44, True, 'eert')


def func_2(**kwargs):
    print(kwargs)


func_2(c=12, a=3, d=5, f=44, s=0, r=55)


def func_3(*args, **kwargs):
    print('-' * 50)
    print(args)
    print(kwargs)


func_3(5, 7, 'RRR', c=12, a=3, d=5, f=44, s=0, r=55)
func_3(c=12, a=3, d=5, f=44, s=0, r=55)
func_3(5, 7, 'RRR')
func_3()

a = {}
print(type(a))
