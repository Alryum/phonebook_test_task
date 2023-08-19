import csv
import locale


class Phonebook:

    def __init__(self, phonebook_file) -> None:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        self.phonebook_file = phonebook_file  # 'phonebook.csv'

    def load_phonebook(self) -> list:
        with open(self.phonebook_file, 'r', newline="") as file:
            reader = csv.DictReader(file)
            return sorted(list(reader), key=lambda x: x['Фамилия'])

    def __save_phonebook(self, entries):
        with open(self.phonebook_file, 'w', newline="") as file:
            fieldnames = ['Фамилия', 'Имя', 'Отчество',
                          'Организация', 'Рабочий телефон', 'Личный телефон']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(entries)
        print('Успешно записано')

    def display_entries(self, entries, page_size=10):
        total_entries = len(entries)
        num_pages = (total_entries + page_size - 1) // page_size

        page = 1
        while True:
            start_idx = (page - 1) * page_size
            end_idx = min(start_idx + page_size, total_entries)

            print(f"{'Фамилия':<15} {'Имя':<15} {'Отчество':<15} {'Организация':<15} {'Рабочий телефон':<15} {'Личный телефон':<15}")
            print('-' * 90)

            for row in entries[start_idx:end_idx]:
                print(f"{row['Фамилия']:<15} {row['Имя']:<15} {row['Отчество']:<15} {row['Организация']:<15} {row['Рабочий телефон']:<15} {row['Личный телефон']:<15}")

            print(f"Страница {page}/{num_pages}")
            user_input = input("Для продолжения нажмите Enter, либо введите 'q' для выхода: ")

            if user_input.lower() == 'q':
                break

            page += 1
            if page > num_pages:
                page = 1

    def __entry_generator(self):
        entry = {
            'Фамилия': input('Введите фамилию: '),
            'Имя': input('Введите имя: '),
            'Отчество': input('Введите отчество: '),
            'Организация': input('Введите название организации: '),
            'Рабочий телефон': input('Введите рабочий телефон: '),
            'Личный телефон': input('Введите личный телефон: '),
        }
        return entry

    def add_entry(self, entries):
        new_entry = self.__entry_generator()
        entries.append(new_entry)
        self.__save_phonebook(entries)

    def edit_entry(self, entries):
        entries_for_edit = self.search_entries(entries)

        print(f"{'id':<4} {'Фамилия':<15} {'Имя':<15} {'Отчество':<15} {'Организация':<15} {'Рабочий телефон':<15} {'Личный телефон':<15}")
        print('-' * 94)
        ids = set()
        for d in entries_for_edit:
            for i, row in d.items():
                print(
                    f"{i:<4} {row['Фамилия']:<15} {row['Имя']:<15} {row['Отчество']:<15} {row['Организация']:<15} {row['Рабочий телефон']:<15} {row['Личный телефон']:<15}")
                ids.add(i)
            while True:
                choice = int(input('Выберите id записи, которую необходимо изменить: '))
                if choice in ids:
                    entries[choice] = self.__entry_generator()
                    self.__save_phonebook(entries)
                    break
                print('Некорректный id')

    def search_entries(self, entries):
        search_criteria = self.__create_search_criteria()
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
                        'Игнорировать[Y/y] или перезапустить поиск с новыми параметрами[N/n]: ')
                    if user_decision.lower() == 'y':
                        force_pass = True
                        break
                    elif user_decision.lower() == 'n':
                        return self.search_entries(entries)
                    else:
                        print('Ожидается [Y/y] или [N/n]')

        return matching_entries

    def __create_search_criteria(self):
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