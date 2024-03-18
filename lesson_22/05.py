nums = [
    ('Jon', 15),
    ('Clarc', 7),
    ('Ban', 18),
    ('Sara', 7),
    ('Nick', 7)
]

nums.sort(key=lambda x: (x[1], x[0]))
print(nums)
