import json


def load_operations(path):
    """
    Чтение данных из файла
    :param path: путь к файлу
    :return: json файл с данными
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)
