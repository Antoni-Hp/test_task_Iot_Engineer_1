from log_analisis import create_excel_with_log_analisis as start


log_path = 'test_task/'     #zmienna, w której podajemy ścieżkę do folderu z logami
excel_file_name = "logs_analysis.xlsx"  # nazwa budowanego pliku excel, ewentualnie ze ścieżką

if __name__ == '__main__':
    start.task(log_path, excel_file_name)
