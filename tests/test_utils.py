import random

import pytest
from src.models import Operation
from src.utils import load_operations, get_instances, get_executed_operations, sort_operations_by_date
from config import OPERATIONS_PATH


def test_load_operations():
    operations = load_operations(OPERATIONS_PATH)
    assert len(operations) == 101

    with pytest.raises(FileNotFoundError):
        operations = load_operations("test.json")


def test_get_instances():
    operations = load_operations(OPERATIONS_PATH)
    operations = get_instances(operations)
    assert isinstance(operations[random.randint(0,100)], Operation)

def test_get_executed_operations():
    operations = load_operations(OPERATIONS_PATH)
    operations = get_instances(operations)
    operations = get_executed_operations(operations)
    assert operations[random.randint(0,100)].state == "EXECUTED"
    for operation in operations:
        assert operation.state == "EXECUTED"

def test_sort_operations_by_date():
    operations = load_operations(OPERATIONS_PATH)
    operations = get_instances(operations)
    operations = get_executed_operations(operations)
    operations = sort_operations_by_date(operations)
    assert operations[0].date > operations[1].date