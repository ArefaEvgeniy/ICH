def show_letters(some_str):
    yield from ''.join([letter for letter in some_str if letter.isalpha()])
                     # ['A', 's', 'd', 'f', 'w'] -> 'Asdfw'


random_str = show_letters('A!sdf 09 _ w')
print(next(random_str))
print(next(random_str))
print(next(random_str))
print(next(random_str))
print(next(random_str))
# print(next(random_str))
