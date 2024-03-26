# Дан список стран и городов каждой страны. Затем даны названия городов. Для
# каждого города укажите, в какой стране он находится. Пример словаря:
# {“Russia”: “Moscow Petersburg Novgorod Kaluga”, “Ukraine”: “Kiev Donetsk Odessa”}.
# which_country(“Novgorod”) = Russia.

countries = {"Russia": "Moscow Petersburg Novgorod Kaluga", "Ukraine": "Kiev Donetsk Odessa"}
countries_2 = {item.title(): key for key, value in countries.items() for item in value.split()}


def which_country(city):
    for country, cities in countries.items():
        if city in cities:
            return country


def which_country_2(city):
    return countries_2.get(city.title())


print(which_country("Novgorod"))
print(which_country("Kiev"))
print(which_country("Bergheim"))

print('-' * 100)

print(which_country_2("Novgorod"))
print(which_country_2("Kiev"))
print(which_country_2("Bergheim"))
