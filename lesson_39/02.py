class MyClass:
    general_attr = 5
    _private_attr = 7
    __safe_attr = 8

    def my_method(self):
        return self.__safe_attr


my_obj = MyClass()
print(my_obj.general_attr)
print(my_obj._private_attr)
print(my_obj.my_method())
print(my_obj._MyClass__safe_attr)
