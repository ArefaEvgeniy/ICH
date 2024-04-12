import re

text = "Hello, how are you?"

if match := re.search(r"\b\w{3}\b", text):
    print("Match found:", match.group(0))
else:
    print("No match")


x = 10
y = x - 5
if y:
    print(y)
else:
    print('ZERO')


x = 10
if y := x - 5:
    print(y)
else:
    print('ZERO')
