# Напишите функцию highlight_keywords(text, keywords), которая выделяет все
# вхождения заданных ключевых слов в тексте, окружая их символами *.
# Функция должна быть регистронезависимой при поиске ключевых слов.
#
# Пример использования:
# text = "This is a sample text. We need to highlight Python and programming."
#
# keywords = ["python", "programming"]
# highlighted_text = highlight_keywords(text, keywords)
# print(highlighted_text)
# # Вывод: "This is a sample text. We need to highlight *Python* and *programming*."

import re


def highlight_keywords(text, keywords):
    for k in keywords:
        text = re.sub(f"({k})", r'*\1*', text, flags=re.IGNORECASE)
    return text


text = "This is a sample text. We need to highlight Python and programming."

keywords = ["python", "programming"]

print(highlight_keywords(text, keywords))
