string = 'Hello, world!'

new_string = ''
for index, item in enumerate(string):
    print(item)
    if index in (3, 7, 9):
        new_string += item

print(new_string)
