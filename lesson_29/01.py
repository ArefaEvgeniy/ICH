x = 10
a = 5
b = 5

try:
    print('start')
    y = x / (a - b)
except TypeError:
    print('except TypeError')
    y = 1
except ZeroDivisionError:
    print('except ZeroDivisionError')
    y = 0
except (IndexError, ZeroDivisionError):
    print('except IndexError')
    y = 100

print('y:', y)

print('end')

...
