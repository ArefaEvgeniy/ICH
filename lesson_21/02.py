matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # 6

print(matrix[2][2])

a = (3, [5, 3], 7, [[9, 2], [1, 2, 3]])

print(a[3][1][0])  # a[3] -> [[9, 2], [1, 2, 3]]  a[3][1] -> [1, 2, 3]  a[3][1][0] -> 1

numbers = ('0', '1', '3', '14', '2', '7', '9', '8', '10')
print(numbers[3][1])
print(type(numbers[3][1]))