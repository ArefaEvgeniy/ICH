file = open("example.txt")
string = file.read()
file.close()

file = open("example.txt", "r")
string_2 = file.readline()
string_3 = file.readline()
file.close()

file = open("example.txt")
string_all = file.readlines()
file.close()

print(string)
print(string_2.strip())
print(string_3.strip())
print(string_all)
