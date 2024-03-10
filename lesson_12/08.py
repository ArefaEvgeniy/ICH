str_1 = '    Hello, world! '
str_2 = 'Hello, !!!! world!!!!!'
str_3 = 'Hello, world'

new_1 = str_1.strip(' ')
new_2 = str_1.strip()
new_3 = str_2.strip('!')

new_4 = str_1.lstrip()
new_5 = str_1.rstrip()

new_6 = str_2.lstrip('!')
new_7 = str_2.rstrip('!')

print(new_1)
print(new_2)
print(new_3)
print(new_4)
print(new_5)
print(new_6)
print(new_7)

leight_1 = len(str_2)
new_str = str_2.rstrip('!')
leight_2 = len(new_str)
if leight_1 > leight_2:
    new_str += '!'
print(new_str)

leight_1 = len(str_3)
new_str = str_3.rstrip('!')
leight_2 = len(new_str)
if leight_1 > leight_2:
    new_str += '!'
print(new_str)

print(str_3.strip('Hello'))
