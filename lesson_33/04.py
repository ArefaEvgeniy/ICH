from typing import List, Tuple, Set, Dict, Union


def process_data(data: List[str]) -> Tuple[int, Set[str]]:
    # Обработка данных
    return len(data), set(data)


def get_person_details(person: Dict[str, Union[str, int]]) -> str:
    # Получение информации о человеке
    return f"{person['name']}, {person['age']} years old"
