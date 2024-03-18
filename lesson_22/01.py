import copy

def newlist(s, a):
    print('s:', s)
    print('a:', a)
    a += 1
    s.append(a)

    print(s, a)


k = [1, 2]
b = 3
print('s:', k)
print('a:', b)
newlist(k[:], b)
newlist(copy.copy(k), b)
print('k:', k)
print('b:', b)
