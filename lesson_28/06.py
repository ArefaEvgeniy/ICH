from collections import Counter


my_list = [1, 2, 3, 1, 2, 3, 1, 2, 4, 5, 4, 3]
my_counter = Counter(my_list)
print(my_counter)   # Выводит Counter({1: 3, 2: 3, 3: 3, 4: 2, 5: 1})
print(my_counter[1])  # Выводит 3, так как элемент "1" встречается 3 раза в списке
print(my_counter[5])

count_1 = {}
for item in my_list:
    if item in count_1:
        count_1[item] += 1
    else:
        count_1[item] = 1

print(count_1)
