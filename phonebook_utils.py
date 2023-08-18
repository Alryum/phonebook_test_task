import csv
import locale

phonebook_file = 'phonebook.csv'
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def load_phonebook() -> list:
    with open(phonebook_file, 'r', newline="") as file:
        reader = csv.DictReader(file)
        return sorted(list(reader), key=lambda x: x['Фамилия'])


def save_phonebook(entries):
    with open(phonebook_file, 'w', newline="") as file:
        fieldnames = ['Фамилия', 'Имя', 'Отчество',
                      'Организация', 'Рабочий телефон', 'Личный телефон']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)
    print('Успешно добавлено')


def display_entries(entries):
    print(f"{'Фамилия':<15} {'Имя':<15} {'Отчество':<15} {'Организация':<15} {'Рабочий телефон':<15} {'Личный телефон':<15}")
    print('-' * 90)
    for row in entries:
        print(f"{row['Фамилия']:<15} {row['Имя']:<15} {row['Отчество']:<15} {row['Организация']:<15} {row['Рабочий телефон']:<15} {row['Личный телефон']:<15}")
    input('Нажмите для продолжения...')


def add_entry(entries):
    entry = {
        'Фамилия': input('Введите фамилию: '),
        'Имя': input('Введите имя: '),
        'Отчество': input('Введите отчество: '),
        'Организация': input('Введите название организации: '),
        'Рабочий телефон': input('Введите рабочий телефон: '),
        'Личный телефон': input('Введите личный телефон: '),
    }
    entries.append(entry)
    save_phonebook(entries)


def edit_entry(entries,  first_name, last_name):
    for entry in entries:
        if entry["Фамилия"].lower() == last_name.lower() and entry["Имя"].lower() == first_name.lower():
            entry["Фамилия"] = input("Введите новую фамилию: ")
            entry["Имя"] = input("Введите новое имя: ")
            entry["Отчество"] = input("Введите новое отчество: ")
            entry["Организация"] = input("Введите новое название организации: ")
            entry["Рабочий телефон"] = input("Введите новый рабочий телефон: ")
            entry["Личный телефон"] = input("Введите новый личный телефон: ")
            save_phonebook(entries)
            print("Запись успешно обновлена.")


def search_entries(entries, search_criteria):
    matching_entries = []

    for entry in entries:
        match = True
        for key, value in search_criteria.items():
            if entry.get(key, "").lower() != value.lower():
                match = False
                break
        if match:
            matching_entries.append(entry)

    return matching_entries


def create_search_criteria():
    search_criteria = {}
    print('Значения опциональны. Оставить поле пустым при необходимости.')
    last_name = input('Фамилия: ')
    first_name = input('Имя: ')
    patronymic = input('Отчество: ')
    organization = input('Организация: ')
    work_phone = input('Рабочий телефон: ')
    personal_phone = input('Личный телефон: ')

    if last_name:
        search_criteria['Фамилия'] = last_name
    if first_name:
        search_criteria['Имя'] = first_name
    if patronymic:
        search_criteria['Отчество'] = patronymic
    if organization:
        search_criteria['Организация'] = organization
    if work_phone:
        search_criteria['Рабочий телефон'] = work_phone
    if personal_phone:
        search_criteria['Личный телефон'] = personal_phone

    return search_criteria
