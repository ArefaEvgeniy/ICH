print('red', 'green', 667, end='!\n', sep=',')
print(44)
print(end=' ')
print('SUN', sep=',')

f = open('test.txt', 'w')
print('red', 'green', 667, end='!\n', sep=',', file=f)
f.close()
