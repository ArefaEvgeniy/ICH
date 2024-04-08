class Parent:
    def func_1(self):
        ...

    def func_2(self):
        ...


class MyClass_1(Parent):
    def __next__(self):
        pass


class MyClass_2(Parent):
    def __next__(self):
        pass


class MyClass_3(Parent):
    def __next__(self):
        pass

    def func_1(self):
        pass
