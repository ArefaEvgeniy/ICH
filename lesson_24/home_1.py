# Написать программу, вычисляющую факториал числа.
# Решить задачу с помощью рекурсии.

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


N = int(input("Введите N: "))
print(f"{N}! = {fact(N)}")
