class MyClass(object):
    def func_0(self):
        print('func_0')

    def func_1(self):
        print('func_1')

    def func_2(self):
        print('func_2')


class MyClass_1(MyClass):
    def func_1(self):
        print('new func_1')

    def func_3(self):
        print('func_3 from MyClass_1')

    def func_4(self):
        print('func_4')


class MyClass_2(MyClass):
    def func_2(self):
        print('new func_2')

    def func_3(self):
        print('func_3 from MyClass_2')

    def func_5(self):
        print('func_5')


class NewClass(MyClass_1, MyClass_2):
    pass


obj_1 = NewClass()
obj_1.func_1()
obj_1.func_2()
obj_1.func_3()
obj_1.func_4()
obj_1.func_5()
obj_1.func_0()
