# Напишите генератор, который будет генерировать арифметическую прогрессию

def ar_prog(a1, d, size):
    count = 1
    while count <= size:
        yield a1
        a1 += d
        count += 1


for i in ar_prog(1, 2, 10):
    print(i)
