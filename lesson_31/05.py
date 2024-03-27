def my_generator():
    n = 1
    while True:
        yield n
        n += 1


my_list = []
for item in my_generator():
    print(item)
    my_list.append(item)
