import json

def open_json_file(json_file):

    with open(json_file) as file:
        return json.load(file)

def filter_of_EXECUTED_operations(operations_data):

    list_of_file = []
    for operation in operations_data:
        if operation['state'] == 'EXECUTED':
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
            masked_number_card = f"{number_card[:4]} {number_card[4:6]}** **** {number_card[:-4]} ->"
            return f"{(' '.join(parts[:-1]))} {masked_number_card}"
        if len(number_card) == 20:
            masked_number_card = f"**{number_card[-4:]}"
            return f"{(' '.join(parts[:-1]))} {masked_number_card}"
    return f"Без номера ->"

def mask_operation_to(operation_to):
    operation_f = operation_to.get('from')
    if operation_f:
        parts = operation_f.split(" ")
        number_card = parts[-1]
        if len(number_card) == 16:
            masked_number_card = f"{number_card[:4]} {number_card[4:6]}** **** {number_card[:-4]} ->"
            return f"{(' '.join(parts[:-1]))} {masked_number_card}"
        if len(number_card) == 20:
            masked_number_card = f"**{number_card[-4:]}"
            return f"{(' '.join(parts[:-1]))} {masked_number_card}"
    return f"Без номера"