nums = [
    ('Jon', 15),
    ('Clarc', 7),
    ('Ban', 18),
    ('Sara', 7),
    ('Nick', 7)
]

new_nums = sorted(nums, key=lambda x: (x[1], x[0]))
print(nums)
print(new_nums)

nums.reverse()
print(nums)

new_nums_2 = list(reversed(new_nums))
print(new_nums)
print(new_nums_2)
