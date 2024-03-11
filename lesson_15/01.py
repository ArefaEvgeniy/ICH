string = 'Hello, world!'

count = 0
while count < len(string):
    print(string[count])
    count += 1

print('-' * 100)

for item in string:
    if item == ' ':
        continue
    elif item.lower() == 'r':
        break
    print(item)
else:
    print('END')
