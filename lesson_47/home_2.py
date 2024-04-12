# Напишите функцию find_common_words(url_list), которая принимает список
# URL-адресов и возвращает список наиболее часто встречающихся слов на
# веб-страницах. Для каждого URL-адреса функция должна получить содержимое
# страницы с помощью запроса GET и использовать регулярные выражения для
# извлечения слов. Затем функция должна подсчитать количество вхождений
# каждого слова и вернуть наиболее часто встречающиеся слова в порядке
# убывания частоты.

import requests
import re
from collections import Counter


def find_common_words(url_list):
    text = ""
    for url in url_list:
        response = requests.get("https://" + url)
        text += response.text
    words = re.findallа(r"\b[a-zA-Zа-яА-ЯёЁ]+\b", text)
    for key, value in Counter(words).most_common(5):
        print(f"{key} {value}")


find_common_words(["realpython.com", "example.com", "pythonru.com"])
