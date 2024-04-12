# Напишите функцию extract_emails(text), которая извлекает все адреса
# электронной почты из заданного текста и возвращает их в виде списка.
#
# Пример использования:
# text = "Contact us at info@example.com or support@example.com for assistance."
#
# emails = extract_emails(text)
# print(emails)  # Вывод: ['info@example.com', 'support@example.com']

import re


def extract_emails(text):
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return emails


s = 'По всем вопросам пишите на vasiliy-1@gma.il.com, или на second.email@yandex.ru, отвечу сразу. Или пишите моему ассистенту secretary@gmail.com!'

for email in extract_emails(s):
    print(email)
