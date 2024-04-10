import re


string = 'AV is largest Analytics AV community of India AV'
result = re.search('Analytics', string)
print(result)
if not result is None:
    print(result.start())
    print(result.end())
    print(result.group(0))


string = 'A190V is largest333 An6666alytics A556V community 55 AV of India A1V'
result = re.findall(r'A(\d+)V', string)
print(result)

string = 'A190V is largest333 An6666alytics A556V community 55 AV of India A1V'
result = re.split(r'A\d+V', string)
print(result)

string = 'A190V is largest333 An6666alytics A556V community 55 AV of India A1V'
result = re.sub(r'A\d+V', '!!!', string)
print(result)

string = 'A190V is  largest333     An6666alytics               A556V   community'
result = re.sub(r'\s+', ' ', string)
print(result)
