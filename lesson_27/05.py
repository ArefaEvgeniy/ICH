def func(a=None):
    if a is None:
        a = [5, 4, 2]
    a.append(len(a))
    return a


c = func([1, 2, 3])
print(c)
func(c)
print(c)

d = func()
print(d)

e = func([6, 6])
print(e)
func(e)

w = func()
print(w)

r = func()
print(r)

t = func()
print(t)
