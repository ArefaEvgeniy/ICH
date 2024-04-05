# Напишите программу, которая принимает в качестве аргумента командной строки
# путь к файлу .py и запускает его. При запуске файла программа должна выводить
# сообщение "Файл <имя файла> успешно запущен". Если файл не существует или не
# может быть запущен, программа должна вывести соответствующее сообщение об ошибке.

import sys
import os.path

args = sys.argv
if len(args) > 1 and os.path.exists(args[1]):
    if os.path.isfile(args[1]):
        if len(args[1]) > 3 and args[1][-3:] == ".py":
            os.system("python "+args[1])
            print("File "+args[1]+" is executed")
        else:
            print("Not a .py file")
    else:
        print("Not a file")
else:
    print("File doesn't exist")
