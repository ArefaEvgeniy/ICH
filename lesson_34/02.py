my_str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.'


def my_generator(string):
    data = string.split()
    for item in data:
        yield item.title().replace('.', '').replace(',', '')


def my_generator_2(string):
    yield from [item.title().replace('.', '').replace(',', '') for item in string.split()]


gen = my_generator_2(my_str)
for item in gen:
    print(item)
