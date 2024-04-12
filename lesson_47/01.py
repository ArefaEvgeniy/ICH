import requests


response = requests.get("https://rozetka.com.ua/ua/notebooks/c80004/")
print(response.status_code)
print(response.headers)
# print(response.text)
