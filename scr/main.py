import json

def open_json_file(json_file):

    with open(json_file) as file:
        return json.load(file)