from operator import itemgetter


data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20}
]


def my_sort(item):
    return item['name'][2]


sorted_data = sorted(data, key=my_sort)
print(sorted_data)
