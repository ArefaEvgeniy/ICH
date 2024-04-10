# Вернуть домены из списка email-адресов
# 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'

import re

string = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'
result = re.findall(r'@\w+.\w+', string)
print(result)
