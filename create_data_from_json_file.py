import json
import os


def get_data_and_headers(path):
    file = (os.listdir(path))
    data = _upload_json_to_table(_collect_json_file(file), path)  #wypakowanie wszystkich plików json do słownika
    return data


def _collect_json_file(file):
    json_files = []
    for logs_name in file:
        if logs_name.endswith(".json"):    #weryfikacja czy plik ma rozszerzenie json
            json_files.append(logs_name)
    return json_files


def _upload_json_to_table(file, path):
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
