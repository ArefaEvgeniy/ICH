class MyIter:
    def __init__(self, value):
        self.value = value.split()
        self.count = -1

    def __next__(self):
        self.count += 1
        if self.count < len(self.value):
            return self.value[self.count]
        raise StopIteration


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

    def __iter__(self):
        return MyIter(self)


a = MyString('Pine apple applepine')

for item in a:
    print(item)