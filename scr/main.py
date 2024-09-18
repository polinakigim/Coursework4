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