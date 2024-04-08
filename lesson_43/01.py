class MyString(str):

    def __sub__(self, other):
        return self.replace(str(other), '', 1)

    def __add__(self, other):
        # return f'{self}{str(other)}'
        return super().__add__(str(other))

    def __len__(self):
        return len(self.split())

    def __call__(self, *args, **kwargs):
        print('This is a function')

    def __bool__(self):
        if self.isdigit():
            return True
        else:
            return False

    def __int__(self):
        return 1 + len(self)


a = MyString('Pine apple applepine')
b = MyString('apple')

print(a)
print(a.upper())
print(a[3:7])

print(a - b)
print(a + 12)
print(b + 12)

c = MyString('34565756')

print(c - 56)
print(c)

print(len(a))
print(len(c))

c()

print(bool(a))
print(bool(b))
print(bool(c))

print(int(a))
