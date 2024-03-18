from collections import deque

queue = deque()
queue.append(10)  # Добавление элемента в стек
queue.append(0)
queue.append(3)
queue.append(4)
print(queue)
first_element = queue.popleft()  # Извлечение первого элемента из очереди
print(first_element)
print(queue)

first_element = queue.popleft()  # Извлечение первого элемента из очереди
print(first_element)
print(queue)

first_element = queue.popleft()  # Извлечение первого элемента из очереди
print(first_element)
print(queue)
