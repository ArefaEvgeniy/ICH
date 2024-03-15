def say_hi():
    global name
    name = 'Tom'
    print('Hello', name, '!')


def say_bye():
    print('Bye', name)


name = 'Evgeniy'

say_hi()
say_bye()
