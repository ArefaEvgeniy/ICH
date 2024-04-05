import time


class Computer:

    def __init__(self):
        self.data = None

    def get_data(self):
        pass

    def prepare_data(self):
        pass

    def print_data(self):
        pass


class CPU(Computer):

    def get_data(self):
        pass

    def prepare_data(self):
        pass


class Memory(Computer):

    def get_data(self):
        pass


class Processes(Computer):

    def get_data(self):
        pass

    def prepare_data(self):
        pass

    def print_data(self):
        pass


class Fun(Computer):

    def get_data(self):
        pass

    def print_data(self):
        pass


def main():
    items = [CPU(), Memory(), Processes(), Fun()]
    while True:
        for item in items:
            item.get_data()
            item.prepare_data()
            item.print_data()
        time.sleep(2)


if __name__ == '__main__':
    main()
