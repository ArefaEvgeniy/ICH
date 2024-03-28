from bisect import bisect_left, bisect_right

data1 = [1, 3, 5, 7, 9]
data2 = [1, 3, 6, 7, 9]

index = bisect_left(data1, 6)  # Результат: 3  -> [1, 3, 5, 6, 7, 9]
index = bisect_right(data1, 6)  # Результат: 3  -> [1, 3, 5, 6, 7, 9]

index = bisect_left(data2, 6)  # Результат: 2  -> [1, 3, 6, 6, 7, 9]
index = bisect_right(data2, 6)  # Результат: 3  -> [1, 3, 6, 6, 7, 9]
