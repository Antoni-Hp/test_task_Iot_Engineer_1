import json
import os


from pprint import pprint

def file_name(path):
    file = (os.listdir(path))
    data = upload_json(check_file(file), path)
    return data


def check_file(file):
    json_file = []
    for logs_name in file:
        if logs_name.endswith(".json") == True:
            json_file.append(logs_name)
    return json_file


def upload_json(file, path):

    all_data=[]
    for file_logs_name in file:
        data = json.load(open(path + file_logs_name))
        all_data.append(data)
    #    print(data)
    #print(all_data)
    return all_data
