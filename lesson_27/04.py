def func_1(a, b, *args, c=34, d='RR', **kwargs):
    print('a:', a)
    print('b:', b)
    print('args:', args)
    print('c:', c)
    print('d:', d)
    print('kwargs:', kwargs)


func_1(12, 44, c=0, q=10)
