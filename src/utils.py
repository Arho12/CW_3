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
    operation_instances = []
    for operation in operations:
        if operation:
            operation_instance = Operation(
                pk=operation["id"],
                state=operation["state"],
                date=operation["date"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                from_=operation.get("from", ""),
                to=operation["to"],
            )
            operation_instances.append(operation_instance)
    return operation_instances


def get_executed_operations(operations):
    """
    Функция для получения выполненных операций
    """
    executed_operation = []
    for operation in operations:
        if operation.state == "EXECUTED":
            executed_operation.append(operation)
    return executed_operation


def sort_operations_by_date(operations):
    return sorted(operations, key=lambda operation: operation.date, reverse=True)
