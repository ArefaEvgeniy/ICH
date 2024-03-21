a_1 = [1, 'RRR', 4, 7, 0, 'rt', '23', 4, 'rt', 4, 1, 'rt']
a_2 = ['1', '2', '1', '4', '2', '5', '4']

new_list = []
for item in a_1:
    if item not in new_list:
        new_list.append(item)
print(new_list)

print(list(set(a_1)))
print(list(set(a_2)))
