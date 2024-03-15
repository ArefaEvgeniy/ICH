a = (1, '3', 22.23, [1, 2, 99], 99, 22.23)  # -> 122aade44424
# 122aade44424  ->  (112344223, 3aaad2234, 3344ca2314, 678995000, 333245436, 767f55AAE3)
# 678995000   ->  [112344223, 555355362, 333245436]

print(a)
print(type(a))

print(len(a))
print('3' in a)

for item in a:
    print(item)

print(a[1])
print(a[1:3])

a[3].append(101)
print(a)
