# Извлечь слова, начинающиеся на гласную:
# 'AV is largest Analytics community of India'

import re


string = 'AV is largest Analytics community of India'
result = re.findall(r'\b[aeiouAEIOU]\w+', string)
print(result)
