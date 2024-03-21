import time


def factorial_1(n):
    q = 0
    result = 1
    while n > q:
        q += 1
        result *= q
    return result


def factorial_2(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_2(n-1)


n = 1500
now = time.time()
print(factorial_1(n))
print('factorial_1:', time.time() - now)

# print('-' * 100)
# now = time.time()
# print(factorial_2(n))
# print('factorial_2:', time.time() - now)
