# Напишите программу, которая принимает в качестве аргумента командной строки
# путь к директории и выводит список всех файлов и поддиректорий внутри этой
# директории. Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории.

import os
import sys

args = sys.argv
os.chdir(args[1])
current_dir = os.getcwd()

for dirpath, dirnames, filenames in os.walk(current_dir):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
