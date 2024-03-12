# Во всех задачах считывайте входные данные через input() и выводите
# ответ через print()


# 1. Написать программу, которая выводит тег вокруг данного текста. Например,
# при вводе тега 'i' и строки 'Hello' получаем '<i>Hello</i>'

teg = input("Введите тег")
line = input("Введите строку")

print(f'<{teg}>{line}</{teg}>')


# 2. Написать программу, которая печатает True, если слова “cat” и “dog” встре-
# чаются в строке одинаковое количество раз (и напечатать false - если разное
# количество раз). 'catdog' → True, 'catcat' → False, '1cat1cadodog' → True

string = input("Enter a text: ")

cat_count = string.count("cat")
dog_count = string.count("dog")

print("The same count of dogs and cats: ", cat_count == dog_count)


# 3. Для данной строки, напечатать строку, где каждый символ повторяется
# дважды. Например, 'The' → 'TThhee', 'AAbb' → 'AAAAbbbb'.

string = input("Enter you string: ")

for i in string:
    print(i*2, end='')
print()


# 4. Напишите программу, которая печатает ценник по параметрам:
# “The price of <product> is “X” Euro”. В строке <product> и <X> - параметры.
# Убедитесь, что цена выводится в Евро с центами
# (не более двух знаков после запятой).

item_name = input("Enter an item name: ")
item_price = float(input("Enter an item price: "))

print(f'The price of {item_name} is "{item_price:.2f}" Euro')


# 5. Дана строка, состоящая из слов, разделенных пробелами. Определите,
# сколько в ней слов. Используйте для решения задачи метод count.

string = input("Enter some worlds separated by whitespace: ").strip()
words_amount = string.count(" ") + 1 if string else 0
print("Amount of words: ", words_amount)


# 6. Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переста-
# вьте эти слова местами. Результат запишите в строку и выведите получившуюся
# строку. При решении этой задачи не стоит пользоваться циклами и инструкцией if.

string = input("Enter two words separated by whitespace: ")
new_string = f"{string.split()[-1]} {string.split()[0]}"
print(new_string)

# 7. Дана строка. Если в этой строке буква f встречается только один раз,
# выведите её индекс. Если она встречается два и более раз, выведите индекс её
# первого и последнего появления. Если буква f в данной строке не встречается,
# ничего не выводите. При решении этой задачи не стоит использовать циклы.

# First variant
string = input("Enter you string ")

first_count = None
second_count = None
for index, item in enumerate(string):
    if item.lower() == 'f':
        if first_count is None:
            first_count = index
            print(f'index of first chair "f" - {first_count}')
        else:
            second_count = index

if second_count is not None:
    print(f'index of last chair "f" - {second_count}')


# Second variant
string = input("Enter you string ")
count = string.count('f')
if count == 1:
    print(string.index('f'))
elif count > 1:
    print(f'first index chair "f" - {string.find("f")} last index {string.rfind("f")}')


# 8. Напишите программу, которая запрашивает у пользователя имя файла
# (переменная file) и целое число (переменная lines), а затем выводит на экран
# построчно строки в количестве lines (на всякий случай проверим, что задано
# положительное целое число). Протестируем функцию на файле article.txt
# со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

file = 'article.txt' #input('Введите файл: ')
lines = input('Введите целое положительное число: ')
if lines.isdigit() and lines != '0':
    with open(file, encoding='utf-8') as file:
        for i in range(int(lines)):
            line = file.readline().strip()
            if line:
                print(line)
