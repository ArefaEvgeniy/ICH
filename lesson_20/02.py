a = [100, '45', 'rr', 0, 0.556]

for index, item in enumerate(a):
    print(index, item)
    if str(item) == '0':
        print('found, index:', index)
else:
    print('END')
