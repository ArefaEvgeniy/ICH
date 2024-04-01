text = 'Любой текст записанный в файл'

# file = open('test.txt', 'w')
# file.write(text)
# file.close()

# file = None
# try:
#     file = open('test.txt', 'w')
#     file.write(text)
# finally:
#     file.close()


with open('test.txt', 'w', encoding='utf-8') as file:
    file.write(text)

with open('test2.txt', 'w') as file:
    file.write(text)

with open('test.txt', 'wb') as file:
    file.write(text.encode('utf-8'))

with open('test.txt', 'rb') as file:
    new_text = file.read()

with open('test2.txt', 'rb') as file:
    new_text_2 = file.read()

print(new_text)
print(new_text_2)
print(type(new_text))

print(new_text.decode())
print(new_text_2.decode('Windows-1251'))
