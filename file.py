import json
import os


def file_name(path):

    file = (os.listdir(path))
    data = upload_json(check_file(file), path)  #wypakowanie wszystkich plików json do słownika
    return data


def check_file(file):

    json_file = []
    for logs_name in file:
        if logs_name.endswith(".json"): #weryfikacja czy plik ma rozszerzenie json
            json_file.append(logs_name)
    return json_file


def upload_json(file, path):

    all_data = []
    headers = []
    for file_logs_name in file:
        data = json.load(open(path + file_logs_name))   # wszystkie dane z logu jako słownik
        all_data.append(data)   #tworzy tabele ze słownikami zawierającymi dane z logów
        data_tmp = (data.keys())  #wszystkie klucze z danego pliku log (nagłówki)
        for keys in data_tmp:
            if keys not in headers:   # sprawdzenie, czy nagłówek jest już w tabeli
                headers.append(keys)   # jeżeli nie to dodaj, tworzy unikatową tabelę z wszystkimi nagłówkami
    return all_data, headers    #zwraca tabele z wszystkimi danymi i nagłówki
