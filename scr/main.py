import json
import datetime as dt

def open_json_file(json_file):
    with open(json_file) as file:
        return json.load(file)

def filter_of_EXECUTED_operations(operations_data):
    list_of_file = []
    for operation in operations_data:
        if operation.get('state') == 'EXECUTED':
            list_of_file.append(operation)
            continue
    return list_of_file


def filter_operations_data(operations_data):
    filter_list = sorted(operations_data, key=lambda x: x['date'], reverse=True)
    return filter_list

def mask_operation_from(operation_from):
    operation_f = operation_from.get('from')
    if operation_f:
        parts = operation_f.split(" ")
        number_card = parts[-1]
        if len(number_card) == 16:
            masked_number_card = f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]} ->"
            return f"{(' '.join(parts[:-1]))} {masked_number_card}"
        if len(number_card) == 20:
            masked_number_card = f"**{number_card[-4:]}"
            return f"{(' '.join(parts[:-1]))} {masked_number_card} ->"
    return f"Без номера ->"

def mask_operation_to(operation_to):
    operation_f = operation_to.get('to')
    if operation_f:
        parts = operation_f.split(" ")
        number_card = parts[-1]
        if len(number_card) == 16:
            masked_number_card = f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
            return f"{(' '.join(parts[:-1]))} {masked_number_card}"
        if len(number_card) == 20:
            masked_number_card = f"**{number_card[-4:]}"
            return f"{(' '.join(parts[:-1]))} {masked_number_card}"
    return f"Без номера"

def formate_date(operation):
    date: str = operation['date']
    dt_time = dt.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return dt_time.strftime("%d.%m.%Y")

def descrtiption_operation(descr):
    if isinstance(descr, dict) and 'description' in descr:
        name_description = descr['description']
        return name_description

def money_count(money):
    for operation in money:
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        return f"{amount} {currency}"


#Передача параметров
data = open_json_file("/home/polina/AccountOperation/Coursework4/data/operations.json")
operations = filter_of_EXECUTED_operations(data)
operations = filter_operations_data(operations)

for i in operations[:5]:
    print(f"{formate_date(i)} {descrtiption_operation(i)}")
    print(f"{mask_operation_from(i)} {mask_operation_to(i)}")
    print(f"{money_count([i])}\n")