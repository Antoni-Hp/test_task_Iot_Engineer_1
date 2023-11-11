import file
import create_excel




def print_hi(name):
    data = file.file_name('test_task/')
    create_excel.dodanie_danych(data)
    #print(file.upload_json())

def Upload_files(filepath):
    date = open(filepath, "r")

if __name__ == '__main__':
    print_hi('PyCharm')


