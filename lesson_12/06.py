str_1 = 'Hello, world! Hello my friends.'
str_2 = 'world'

new_1 = str_1.split(' ')
new_2 = str_2.split(' ')
new_3 = str_1.split('l')
new_4 = str_1.split('llo')

print(new_1)
print(new_2)
print(new_3)
print(new_4)

str_new_1 = ''.join(new_1)
print(str_new_1)

str_new_2 = '---'.join(new_1)
print(str_new_2)
