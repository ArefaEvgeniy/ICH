x = [1, 2, 3]

try:
    print('start')
    y = x[10]
    print('continue')
except TypeError:
    print('except TypeError')
    y = 1
except IndexError:
    print('except IndexError')
    y = 100
except LookupError:
    print('except LookupError')
    y = 0
except Exception as err:
    print('err')
    y = 0
else:
    print('ELSE')
finally:
    print('Finally')

# print('Finally')

print('y:', y)

print('end')

...

try:
    file = open('')
    ...
finally:
    file.close()
