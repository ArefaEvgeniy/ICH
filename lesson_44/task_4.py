# Существует функция coffee(), которая варит кофе и если ее вызвать, то она
# печатает “кофе”. Декорировать эту функцию так, чтобы можно было варить кофе
# с сахаром, молоком или и тем и другим. Вызов декорируемой функции должен
# печатать, с чем кофе сварено. Сварить кофе с двойной порцией сахара и
# молока. Сварить двойной кофе.


def decorator(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("milk") or kwargs.get("suger"):
            print('с', end=' ')
            if kwargs.get("milk"):
                print('двойным молоком', end=' ') if kwargs['milk'] > 1 \
                    else print('молоком', end=' ')
            if kwargs.get("milk") and kwargs.get("suger"):
                print('и', end=' ')
            if kwargs.get("suger"):
                print('двойным сахаром', end=' ') if kwargs['suger'] > 1 \
                    else print('сахаром', end=' ')
        if kwargs.get("double"):
            print('двойной', end=' ')

        func()

    return wrapper


@decorator
def coffe():
    print('кофе')


coffe()
coffe(double=True)
coffe(milk=1)
coffe(milk=2)
coffe(suger=2)
coffe(double=True, suger=1)
coffe(double=True, milk=1, suger=1)
coffe(milk=2, suger=1, double=True)
coffe(suger=2, double=True)
coffe(milk=2, suger=2, double=True)
coffe(milk=1, suger=2, double=False)
