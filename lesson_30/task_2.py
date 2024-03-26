# Дано слово, которое может состоять как из строчных, так и из прописных латинских
# букв. Проверьте, является ли это слово палиндромом. Выведите YES или NO.
# Пример: is_palindrom(“radar”) вернет Yes, is_palindrom(“yes”)  вернет No.

def is_palindrom(word):
    result = 'no'
    if word[::-1].lower() == word.lower():
        result = 'yes'
    return result


print(is_palindrom(input()))
