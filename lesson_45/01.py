class MyClass:

    def general_method(self, a, b):
        print('This is a general method')
        return a + b

    @staticmethod
    def static_method(a, b):
        print('This is a static method')
        return a + b


obj_1 = MyClass()
print(obj_1.general_method(3, 4))
print("-" * 50)
print(MyClass.static_method(3, 4))
print(obj_1.static_method(3, 4))
