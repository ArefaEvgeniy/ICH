from typing import Optional, Union, Any


def add(a: Any, b: Union[int, str, bool]) -> Optional[str]:
    result = None
    if type(a) == str and type(b) == int:
        result = a * b
    elif type(a) == str and type(b) == str:
        result = a + b

    return result


print(add(4, 5))
print(add(4, 'SS'))
print(add('SS', 5))
print(add('RR', 'SS'))
