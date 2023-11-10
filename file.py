import json
import os


from pprint import pprint

def file_name(path):
    file = (os.listdir(path))
    print(check_file(file))


def check_file(file):
    json_file = []
    for logs_name in file:
        if logs_name.endswith(".json") == True:
            json_file.append(logs_name)
    return json_file


def upload_json(file):

    data = json.load(open(file))
    return data
