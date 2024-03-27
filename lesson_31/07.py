import itertools
import sys

my_list = [x for x in range(1000001)]
my_iterator = itertools.islice(my_list, 1, 99999)
my_iterator_2 = iter(my_list)
my_cut = my_list[1:99999]
# del my_list
my_list[1] = -100
my_list[2] = -150
my_list[3] = -200
print(type(my_iterator))
print(sys.getsizeof(my_iterator))
print(type(my_iterator_2))
print(sys.getsizeof(my_iterator_2))
print(type(my_cut))

print(sys.getsizeof(my_iterator))
print(sys.getsizeof(my_cut))

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# print('-' * 50)
# for item in my_iterator:
#     print(item)
#
# print('-' * 50)
# for item in my_cut:
#     print(item)
