import time


def get_data() -> dict | None:
    data = {}

    def get_cpu(data: dict) -> dict:
        ...
        return data

    def get_prossec(data: dict) -> dict:
        ...
        return data

    def get_memory(data: dict) -> dict:
        ...
        return data

    def get_fun(data: dict) -> dict:
        ...
        return data

    data = get_cpu(data)
    data = get_prossec(data)
    data = get_memory(data)
    data = get_fun(data)
    ...
    return data


def prepare_data(data: dict) -> list:
    result = []
    ...
    return result


def print_data(data: list) -> None:
    ...


def main():
    while True:
        data = get_data()
        data = prepare_data(data)
        print_data(data)
        time.sleep(2)


if __name__ == '__main__':
    main()
