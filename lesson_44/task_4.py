# Существует функция coffee(), которая варит кофе и если ее вызвать, то она
# печатает “кофе”. Декорировать эту функцию так, чтобы можно было варить кофе
# с сахаром, молоком или и тем и другим. Вызов декорируемой функции должен
# печатать, с чем кофе сварено. Сварить кофе с двойной порцией сахара и
# молока. Сварить двойной кофе.


def decorator(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("double"):
            print('двойной', end=' ')
        if kwargs.get("milk"):
            print('с', end=' ')
            if kwargs['milk'] > 1:
                print(f'{kwargs["milk"]}-ым', end=' ')
            print('молоком', end=' ')
        if kwargs.get("shuger"):
            print('с', end=' ')
            if kwargs['shuger'] > 1:
                print(f'{kwargs["shuger"]}-ым', end=' ')
            print('сахаром', end=' ')

        func()

    return wrapper


@decorator
def coffe():
    print('кофе')


coffe()
coffe(double=True)
coffe(milk=1)
coffe(milk=2)
coffe(shuger=2)
coffe(double=True, shuger=1)
coffe(double=True, milk=1, shuger=1)
