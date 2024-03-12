string = 'Hello, world!\nSecond line.\nEnd line.'


file = open("example_2.txt", "w")
file.write(string)
file.close()

# file = open("example_2.txt", "a")
# # file.write('\nThis is my text!')
# # file.close()

with open("example_2.txt", "a") as file:
    file.write('\nThis is my text!')

