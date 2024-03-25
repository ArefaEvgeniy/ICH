from collections import namedtuple


air_list_1 = ('A-38', 120, 1971, 'ADE4562')
air_list_2 = ('A-220', 220, 2000, 'RZXE45452')
air_list_3 = ('B-50', 50, 1989, '0035SFGR')
air_list_4 = ('A-55', 90, 1981, 'ZZXDER45')

for item in (air_list_1, air_list_2, air_list_3, air_list_4):
    print(item[3])

Air = namedtuple('Air', ['model', 'sits', 'year', 'number'])
air_1 = Air(model='A-38', sits=120, year=1971, number='ADE4562')
air_2 = Air(model='A-220', sits=220, year=2000, number='RZXE45452')
air_3 = Air(model='B-50', sits=50, year=1989, number='0035SFGR')
air_4 = Air(model='A-55', sits=90, year=1981, number='ZZXDER45')

print(air_1.sits)
print(air_1[1])

print('-' * 50)
for item in (air_1, air_2, air_3, air_4):
    print(item[3])

print('-' * 50)
for item in (air_1, air_2, air_3, air_4):
    print(item.number)
