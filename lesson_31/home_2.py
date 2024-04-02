# Напишите генератор, который будет генерировать бесконечную последовательность
# Фибоначчи. Каждый раз, когда генератор вызывается, он должен возвращать
# следующее число последовательности. Напишите программу, которая будет
# использовать этот генератор для вывода первых N чисел Фибоначчи.
# Пример вывода:
# Введите количество чисел Фибоначчи: 10
# Первые 10 чисел Фибоначчи:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


N = int(input("Введите число: "))
fib_gen = fibonacci_generator()
for i in range(N):
    print(next(fib_gen))
