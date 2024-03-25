x = [1, 2, 3]

try:
    print('start')
    y = x[10]
    print('continue')
except Exception:
    print('except')
    y = 0
else:
    print('ELSE')


print('y:', y)

print('end')

...
