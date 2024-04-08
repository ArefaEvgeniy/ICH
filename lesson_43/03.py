class MyString(str):

    def __next__(self):
        self.count += 1
        if self.count < len(self.split()):
            return self.split()[self.count]
        raise StopIteration

    def __iter__(self):
        self.count = -1
        return self


a = MyString('Pine apple applepine')

for item in a:
    print(item)
