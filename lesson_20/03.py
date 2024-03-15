a = [100, '45', 'rr', 0, 0.556]

for index, item in enumerate(a):
    if str(item) == '0':
        break
    elif str(item) == 'rr':
        continue
    print(item)
else:
    print('END')
