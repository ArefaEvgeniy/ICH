INPUT_LIST = [
    1,
    '2',
    'cat',
    99,
    'dog',
    (4, 44, ['red', 'green', ('mother', 'father',)]),
    ['one', 'two', '55', (1, 4, 'big', True), ['milk', 0, 'bred']],
    'End'
]


def find_word(word, collection):
    result = False

    for item in collection:
        if isinstance(item, (str, int, float)) and word == str(item):
            result = True
            break

        elif isinstance(item, (tuple, list)):
            result = find_word(word, item)
            if result:
                break

    return result


def main():
    input_word = input('Enter your word: ')
    if find_word(input_word, INPUT_LIST):
        print('Found')
    else:
        print('Did not find')


main()
