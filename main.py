import create_data_from_json_file
import create_excel

log_path = 'test_task/'     #zmienna, w której podajemy ściezkę do folderu z logami


def task():
    data = create_data_from_json_file.get_data_and_headers(log_path)     #stworzenie tablicy słowników z danymi pobranymi z plików json
    create_excel.upload_data(data[0], data[1])


if __name__ == '__main__':
    task()
