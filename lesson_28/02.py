dct = {
    'a': 'b',
    'b': 'c',
    'c': 'a'
}

print(dct.get('a'))
print(dct.get(dct.get(dct.get('a'))))
