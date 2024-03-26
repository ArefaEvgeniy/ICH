# Словарь синонимов. Вам дан словарь, состоящий из пар слов. Каждое слово
# является синонимом к парному ему слову. Все слова в словаре различны.
# Написать функцию, которая для заданного слова из словаря, определяет его
# синоним. Пример словаря: {“Hello”: “Hi”, “Bye”: “Goodbye”, “List”: “Array”}.
# get_synonim(“Goodbye”) -> Bye.  get_synonim(“List”) -> Array.

synonyms = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}
synonyms_2 = {value: key for key, value in synonyms.items()}


def get_synonim(word):
    result = None
    if word in synonyms:
        result = synonyms[word]
    for key, value in synonyms.items():
        if word == value:
            result = key
    return result


def get_synonim_2(word):
    result = None
    if word in synonyms:
        result = synonyms[word]
    elif word in synonyms_2:
        result = synonyms_2[word]
    return result


def get_synonim_3(word):
    return synonyms[word] if synonyms.get(word) else synonyms_2[word] \
        if synonyms_2.get(word) else None


print(get_synonim("Goodbye"))
print(get_synonim("List"))
print(get_synonim("Test"))

print('-' * 100)

print(get_synonim_2("Goodbye"))
print(get_synonim_2("List"))
print(get_synonim_2("Test"))

print('-' * 100)

print(get_synonim_3("Goodbye"))
print(get_synonim_3("List"))
print(get_synonim_3("Test"))
