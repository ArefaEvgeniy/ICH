# Напишите программу, которая заменяет в тексте все слова, начинающиеся на
# ‘х’ или ‘f’ на звездочки. При чём количество звёздочек должно равняться
# количеству букв заменяемого слова

import re

string = 'X-ray is not good for health if it\'s often'


def my_def(match):
    return len(match.group(0)) * '*'


print(re.sub(r'\b[xXfF][\w-]+\b', my_def, string))
