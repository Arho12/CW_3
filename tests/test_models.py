from datetime import datetime

import pytest
from src.models import Operation


@pytest.fixture
def operation():
    return Operation(
        pk=441945886,
        date="2019-08-26T10:50:58.294041",
        state="EXECUTED",
        operation_amount={
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }},
        description="Перевод организации",
        from_="Maestro 1596837868705199",
        to="Счет 64686473678894779589"
    )

def test_covert_date(operation):
    assert type(operation.date) == datetime

