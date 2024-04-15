import requests
from bs4 import BeautifulSoup

html = requests.get("https://example.com").text
# Создание объекта Beautiful Soup из HTML-страницы

soup = BeautifulSoup(html, "html.parser")

# Извлечение данных из тегов
title = soup.title.text
links = soup.find_all("a")

print(title)
print(links)
print(links[0].text)
print(links[0]["href"])

# Навигация по структуре документа
parent = soup.find("div").parent
next_sibling = soup.find("div").next_sibling

# Манипуляции с содержимым
new_tag = soup.new_tag("a", href="https://example.com")
soup.body.append(new_tag)

links = soup.find_all("a")
print(links)

h_1 = soup.find("h1").text
print(h_1)

link = links[0]["href"]

print('-' * 50)

html_2 = requests.get(link).text
print(html_2)

soup_2 = BeautifulSoup(html_2, "html.parser")

links_2 = soup_2.find_all("a")
print(links_2)

for link in links_2:
    href = link["href"]
    if href[:4] == "http":
        print(href)
