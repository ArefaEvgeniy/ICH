# Напишите генератор, который принимает на вход поток элементов и выдает
# только уникальные элементы, сохраняя их порядок встречаемости (для уже
# повторяющихся элементов генератор не выдает ничего)

def my_generator(x):
    unic = []
    for item in x:
        if item not in unic:
            unic.append(item)
            yield item


a_1 = 'sjfkhwsdoijcnafj'
a_2 = [1, 43, 8, 1, 22, 1, 43, 1, 0]

for item in my_generator(a_2):
    print(item)
