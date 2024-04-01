import os


print(os.getcwd())
os.chdir('C:\PythonProjects\ICH\ICH\lesson_37')
current_dir = os.getcwd()
print(current_dir)
# files = os.listdir(current_dir)
# for file in files:
#     print(file)
# os.makedirs('new_directory/sub_directory')
for dirpath, dirnames, filenames in os.walk(current_dir):
    for filename in filenames:
        print(os.path.join(dirpath, filename))


