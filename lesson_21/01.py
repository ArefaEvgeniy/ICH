numbers = [1, 2, 3, 4, 5]
# [1, 4, 9, 16, 25]

new_numbers = []
for i in numbers:
    if i > 2:
        new_numbers.append(i ** 2)

print(new_numbers)

new_numbers_2 = [i ** 2 for i in numbers if i > 2]
print(new_numbers_2)
