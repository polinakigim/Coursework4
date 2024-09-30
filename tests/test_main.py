import pytest
import json
import datetime as dt


from scr.main import open_json_file, money_count, descrtiption_operation, formate_date, filter_of_EXECUTED_operations, mask_operation_to ,filter_operations_data, mask_operation_from

@pytest.fixture
def test_data():
    return [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {'state': 'CANCELLED'}, {'state': 'CANCELLED'}, {'state': 'EXECUTED'}]
@pytest.fixture
def test_data1():
    return [{'date': '2023-09-10', 'amount': 100}, {'date': '2023-09-11', 'amount': 200}, {'date': '2023-09-09', 'amount': 50},]


def test_open_json_file(tmp_path):
    json_data = {"key": "value", "number": 123}
    json_file = tmp_path / "test_file.json"

    with open(json_file, 'w') as f:
        json.dump(json_data, f)
    result = open_json_file(json_file)
    assert result == json_data

def test_filter_of_EXECUTED_operations(test_data):
    assert len(filter_of_EXECUTED_operations(test_data)) == 4

def test_filter_operations_data(test_data1):
    result = filter_operations_data(test_data1)
    expected = [{'date': '2023-09-11', 'amount': 200}, {'date': '2023-09-10', 'amount': 100}, {'date': '2023-09-09', 'amount': 50},]
    assert result == expected

def test_mask_operation_from_16():
    data = {'from': 'Visa Gold 5999414228426353'}
    result = mask_operation_from(data)
    expected = "Visa Gold 5999 41** **** 6353 ->"
    assert result == expected

def test_mask_operation_from_20():
    data = {'from': 'Счет 24763316288121894080'}
    result = mask_operation_from(data)
    expected = "Счет **4080 ->"
    assert result == expected

def test_mask_operation_from_empty():
    data = {}
    result = mask_operation_from(data)
    expected = "Без номера ->"
    assert result == expected


def test_mack_operation_to_20():
    data = {"to": "Счет 96291777776753236930"}
    result = mask_operation_to(data)
    expected = "Счет **6930"
    assert result == expected

def test_mack_operation_to_16():
    data = {"to": "Visa Platinum 6086997013848217"}
    result = mask_operation_to(data)
    expected = "Visa Platinum 6086 99** **** 8217"
    assert result == expected

def test_mask_operation_to_empty():
    data = {}
    result = mask_operation_to(data)
    expected = "Без номера"
    assert result == expected

def test_formate_date():
    data = {"date": "2018-12-18T17:07:09.800800"}
    result = formate_date(data)
    expected = "18.12.2018"
    assert result == expected

def test_descrtiption_operation():
    data = {"description": "Перевод с карты на карту"}
    result = descrtiption_operation(data)
    expected = "Перевод с карты на карту"
    assert result == expected

def test_money_count():
    data = [
        {
            'operationAmount': {
                'amount': '19683.25',
                'currency': {'name': 'USD'}
            }
        }
    ]
    result = money_count(data)
    expected = "19683.25 USD"
    assert result == expected