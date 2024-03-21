a_1 = [1, 'RRR', 4, 7, 0, 'rt', '23', 4, 'rt', 4, 1]
a_2 = {1, 'RRR', 4, (7, 0), 'rt', '23'}
a_3 = {0, 1, 2, 3, 4, 5}

print('RRR' in a_2)
print('DDD' in a_2)
print(7 in a_2)
print((7, 0) in a_2)
print(len(a_2))

print('-' * 100)
for item in a_2:
    print(item)

print('-' * 100)
for item in a_3:
    print(item)
