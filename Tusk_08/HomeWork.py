from csv import DictWriter, DictReader
from os.path import exists

def create_file():
    with open('GidePhone.csv', 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()

def get_info():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер: ')
    mas_info = [last_name, first_name, phone_number]
    return mas_info

def write_file(lst):
    res = []
    if exists('GidePhone.csv'):
        with open('GidePhone.csv', 'r', encoding='utf-8') as data:
            f_reader = DictReader(data)
            res = list(f_reader)

    obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
    res.append(obj)

    with open('GidePhone.csv', 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)

def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res

def update_file(lst):
    file_name = 'GidePhone.csv'
    if exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as data:
            f_reader = DictReader(data)
            res = list(f_reader)

        fieldnames = f_reader.fieldnames

        for index, entry in enumerate(res):
            if entry['Фамилия'] == lst[0] and entry['Имя'] == lst[1]:
                res[index]['Номер'] = lst[2]
                break

        with open(file_name, 'w', encoding='utf-8') as data:
            f_writer = DictWriter(data, fieldnames=fieldnames)
            f_writer.writeheader()
            f_writer.writerows(res)

def delete_entry(last_name, first_name):
    file_name = 'GidePhone.csv'
    if exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as data:
            f_reader = DictReader(data)
            res = list(f_reader)

        fieldnames = f_reader.fieldnames

        res = [entry for entry in res if entry['Фамилия'] != last_name or entry['Имя'] != first_name]

        with open(file_name, 'w', encoding='utf-8') as data:
            f_writer = DictWriter(data, fieldnames=fieldnames)
            f_writer.writeheader()
            f_writer.writerows(res)



def file_manager():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('GidePhone.csv'):
                create_file()
            print(read_file('GidePhone.csv'))
        elif command == 'w':
            if not exists('GidePhone.csv'):
                create_file()
            write_file(get_info())
        elif command == 'u':
            last_name = input('Введите фамилию: ')
            first_name = input('Введите имя: ')
            phone_number = input('Введите номер: ')
            update_file([last_name, first_name, phone_number])
        elif command == 'd':
            last_name = input('Введите фамилию: ')
            first_name = input('Введите имя: ')
            delete_entry(last_name, first_name)

file_manager()