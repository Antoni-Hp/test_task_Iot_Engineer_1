import file
import create_excel

log_patch = 'test_task/'     #zmienna, w której podajemy ściezkę do folderu z logami


def task():

    data = file.file_name(log_patch)
    create_excel.upload_data(data[0], data[1])


if __name__ == '__main__':

    task()
