import json

from src.models import Operation


def load_operations(path):
    """
    Чтение данных из файла
    :param path: путь к файлу
    :return: json файл с данными
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_instances(operations):
    """
    Создает экземпляры класса Operation
    """
    operations_instances = []
    for operation in operations:
        if operation:
            operations_instance = Operation(
                pk=operation["id"],
                date=operation["date"],
                state=operation["state"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                from_=operation.get("from", ""),
                to=operation["to"],
            )
            operations_instances.append(operations_instance)
    return operations_instances


def get_executed_operations(operations):
    """
    Функция для получения выполненных операций
    """
    executed_operation = []
    for operation in operations:
        if operation.state == "EXECUTED":
            executed_operation.append(operation)
    return executed_operation
