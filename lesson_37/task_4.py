# Дана последовательность слов. Написать функцию, которая возвращает 
# последовательность слов, в которой в словах длины 3 все буквы заглавные, 
# а все слова начинающиеся на "q" или "f" исключены. Использовать цепочки.
# Пример: ["The", "quick", "brown", "fox"] -> ["THE", "quick"]

def funk2(words_list):
    return map(lambda x: x.upper() if len(x) == 3 else x, filter(lambda x: not x.startswith(('q', 'f')), words_list))


words = ["The", "quick", "brown", "fox"]

print(list(funk2(words)))
