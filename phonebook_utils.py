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
    print('Успешно записано')


def display_entries(entries):
    print(f"{'Фамилия':<15} {'Имя':<15} {'Отчество':<15} {'Организация':<15} {'Рабочий телефон':<15} {'Личный телефон':<15}")
    print('-' * 90)
    for row in entries:
        print(f"{row['Фамилия']:<15} {row['Имя']:<15} {row['Отчество']:<15} {row['Организация']:<15} {row['Рабочий телефон']:<15} {row['Личный телефон']:<15}")
    input('Нажмите для продолжения...')


def entry_generator():
    entry = {
        'Фамилия': input('Введите фамилию: '),
        'Имя': input('Введите имя: '),
        'Отчество': input('Введите отчество: '),
        'Организация': input('Введите название организации: '),
        'Рабочий телефон': input('Введите рабочий телефон: '),
        'Личный телефон': input('Введите личный телефон: '),
    }
    return entry


def add_entry(entries):
    entries.append(entry_generator())
    save_phonebook(entries)


def edit_entry(entries):
    entries_for_edit = search_entries(entries)

    print(f"{'id':<4} {'Фамилия':<15} {'Имя':<15} {'Отчество':<15} {'Организация':<15} {'Рабочий телефон':<15} {'Личный телефон':<15}")
    print('-' * 94)
    ids = set()
    for d in entries_for_edit:
        for i, row in d.items():
            print(
                f"{i:<4} {row['Фамилия']:<15} {row['Имя']:<15} {row['Отчество']:<15} {row['Организация']:<15} {row['Рабочий телефон']:<15} {row['Личный телефон']:<15}")
            ids.add(i)
        while True:
            choice = int(input('Выберите id записи, которую необходимо изменить'))
            if choice in ids:
                entries[choice] = entry_generator()
                save_phonebook(entries)
                break
            print('Некорректный id')


def search_entries(entries):
    search_criteria = create_search_criteria()
    matching_entries = []
    force_pass = False

    for i, entry in enumerate(entries):
        match = True
        for key, value in search_criteria.items():
            if entry.get(key, "").lower() != value.lower():
                match = False
                break
        if match:
            matching_entries.append({i: entry})
        if not force_pass and len(matching_entries) > 10:
            print(f'Результаты поиска дают слишком много значений (>10) и поиск ещё не закончен.')
            while not force_pass:
                user_decision = input(
                    'Игнорировать[Y/y] или перезапустить поиск с новыми параметрами[N/n] ?')
                if user_decision.lower() == 'y':
                    force_pass = True
                    break
                elif user_decision.lower() == 'n':
                    return search_entries(entries)
                else:
                    print('Ожидается [Y/y] или [N/n]')

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
