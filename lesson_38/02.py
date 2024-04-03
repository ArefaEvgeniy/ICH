numbers = [1, 2, 3, 4, 5]

# Comprehension
squared = [x ** 2 for x in numbers]  # [1, 4, 9, 16, 25]

# Map-Filter
squared = list(map(lambda x: x ** 2, numbers))  # [1, 4, 9, 16, 25]

# Loop with condition
squared = []
for x in numbers:
    squared.append(x ** 2)  # [1, 4, 9, 16, 25]
