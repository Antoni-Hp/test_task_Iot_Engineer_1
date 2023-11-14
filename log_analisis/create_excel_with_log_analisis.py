from log_analisis import create_data_from_json_file, create_excel


def task(log_path, excel_file_name):
    data = create_data_from_json_file.get_data_and_headers(log_path)     #stworzenie tablicy słowników z danymi pobranymi z plików json
    create_excel.upload_data(data[0], data[1], excel_file_name)