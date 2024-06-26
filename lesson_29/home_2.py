# Напишите программу, которая открывает файл, считывает его содержимое и
# выполняет операции над числами в файле. Обработайте возможные исключения
# при открытии файла (FileNotFoundError) и при выполнении операций над числами
# (ValueError, ZeroDivisionError). Используйте конструкцию try-except-finally
# для обработки исключений и закрытия файла в блоке finally.

try:
    f = open("hw22.txt", "r")
except FileNotFoundError:
    print("Файл не найден")
else:
    try:
        s = [int(i) for i in f.readlines()]
        print(s[0]/s[1])
    except ValueError:
        print("Некорректные данные в файле")
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
    finally:
        f.close()
