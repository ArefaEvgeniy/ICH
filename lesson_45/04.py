from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def method(self):
        pass

    def func(self):
        print('func')


class ConcreteClass(AbstractClass):
    def method(self):
        print("ConcreteClass method")


obj = ConcreteClass()
obj.method()  # ConcreteClass method
