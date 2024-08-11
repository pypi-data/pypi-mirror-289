import time
from functools import wraps
import os
import re


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def tcached(t: int = None):
    _instances = {}

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            input_ = (args, tuple(sorted(kwargs.items())))
            current_time = time.time()
            if input_ not in _instances or (t and _instances[input_][1] + t < current_time):
                _instances[input_] = (func(*args, **kwargs), current_time)
            return _instances[input_][0]
        return inner
    return wrapper


def check_and_create_path(path: str) -> str:
    if path:
        path = path.replace('\\', '/')
        if not os.path.exists(path):
            os.makedirs(path)
        if not path.endswith('/'):
            path += '/'
    return path


def get_next_filename(directory: str, prefix: str, suffix: str) -> str:
    """
    Находит следующий доступный файл в директории с заданным префиксом и постфиксом.

    :param directory: Путь к директории
    :param prefix: Префикс имени файла
    :param suffix: Постфикс имени файла
    :return: Следующее доступное имя файла
    """
    pattern = re.compile(fr'{re.escape(prefix)}(\d+){re.escape(suffix)}')
    max_number = -1

    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            if number > max_number:
                max_number = number

    next_number = max_number + 1
    return f'{prefix}{next_number:03}{suffix}'
