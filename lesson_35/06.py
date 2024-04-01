import os


dir_1 = 'C:\PythonProjects\ICH\ICH\lesson_37'
dir_2 = 'C:\PythonProjects\ICH\ICH\lesson_37\\'

file = 'test.txt'

print(''.join((dir_1, file)))
print(''.join((dir_2, file)))

print('-' * 50)

print(os.path.join(dir_1, file))
print(os.path.join(dir_2, file))
