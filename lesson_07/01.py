# Если х положительный, то х  увеличиваем на 1.
# Если x отрицательный, то в него присваиваем 0.
# В противном случае x выводим на экран


x = int(input())


if x > 10:
    x += 2
elif x > 0:
    x += 1
elif x < 0:
    x = 0
else:
    print(x)
