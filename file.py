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

    all_data = []
    headers = []
    for file_logs_name in file:
        data = json.load(open(path + file_logs_name)) # wszystkie dane z logu jako słownik
        all_data.append(data)   #tworzy tabele z słownikami zawierajacymi dane z logów
        data_tmp=(data.keys())  #wszystkie klucze z danego logu - nagłówki
        for i in data_tmp:
            if not i in headers :   #sprawdzenie czy nagłówek jest już w tabeli
                headers.append(i)   # jeżeli nie to dodaj - tworzy unikatową tabele z wszystkimi nagłówkami
    return all_data, headers    #zwraca tabele z wszystkimi danymi i nagłówki
