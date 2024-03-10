import time
# from time import time, sleep

start = time.time()

number = 1500
count = 1
result = 1
time.sleep(3)
while number >= count:
    result *= count
    count += 1

end = time.time()

print('Факториал =', result)
print('Времени затрачено:', end - start)
