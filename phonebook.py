import csv
import locale
from typing import Dict, List


class Phonebook:
    """
    A class representing a phonebook with various functionalities.
    """

    FIELDS = ['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']

    def __init__(self, phonebook_file: str) -> None:
        """
        Initialize a Phonebook instance.

        Args:
        phonebook_file (str): The path to the CSV file containing phonebook data.
        """

        self.phonebook_file = phonebook_file

    def load_phonebook(self) -> List[Dict[str, str]]:
        """
        Load phonebook entries from a CSV file.

        Returns:
        List[Dict[str, str]] A list of dictionaries representing phonebook entries.
        """

        with open(self.phonebook_file, 'r', newline="") as file:
            locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
            reader = csv.DictReader(file)
            return sorted(list(reader), key=lambda x: x['Фамилия'])

    def display_entries(self, entries: List[Dict[str, str]], page_size=10) -> None:
        """
        Display phonebook entries with pagination.

        Args:
        entries(List[Dict[str, str]]): List of phonebook entries to display.
        page_size(int): Number of entries to display per page.
        """

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
            user_input = input(
                "Далее[Enter], Предыдущая страница: ввести 'prev', либо 'q' для выхода: ")

            if user_input.lower() == 'q':
                break
            elif user_input.lower() == 'prev':
                page -= 1
            else:
                page += 1
            if page > num_pages or page <= 0:
                page = 1

    def add_entry(self, entries: List[Dict[str, str]]) -> None:
        """
        Add a new entry to the phonebook.

        Args:
        entries(List[Dict[str, str]]): List of phonebook entries to append the new entry to.
        """

        new_entry = self.__create_criteria(strong=True)
        entries.append(new_entry)
        self.__save_phonebook(entries)

    def edit_entry(self, entries: List[Dict[str, str]]) -> None:
        """
        Edit an existing phonebook entry.

        Args:
        entries(List[Dict[str, str]]): List of phonebook entries to edit.
        """

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
                new_entry = self.__get_new_entry(entries[choice].copy())
                entries[choice] = new_entry
                self.__save_phonebook(entries)
                break
            print('Некорректный id')

    def search_entries(self, entries: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Search for phonebook entries based on given criteria.

        Args:
        entries(List[Dict[str, str]]): List of phonebook entries to search within.

        Returns:
        List of dictionaries representing matching phonebook entries.
        """

        search_criteria = self.__create_criteria()
        matching_entries = []
        force_pass = False

        for i, entry in enumerate(entries):
            match = True
            for key, value in search_criteria.items():
                if entry.get(key, '').lower() != value.lower():
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

    # PRIVATE METHODS

    def __save_phonebook(self, entries: List[Dict[str, str]]) -> None:
        """
        Save phonebook entries to the CSV file.

        Args:
        entries(List[Dict[str, str]]): List of phonebook entries to save.
        """

        with open(self.phonebook_file, 'w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=Phonebook.FIELDS)
            writer.writeheader()
            writer.writerows(entries)
        print('Успешно записано')

    def __get_new_entry(self, entry: Dict[str, str]) -> Dict[str, str]:
        """
        Create a new phonebook entry based on user input.

        Args:
        entry(Dict[str, str]): Dictionary representing an existing phonebook entry.

        Returns:
        Dict[str, str]: Dictionary representing the new phonebook entry.
        """

        user_edit_fields = self.__create_criteria()

        for key, val in user_edit_fields.items():
            entry[key] = val

        return entry

    def __create_criteria(self, strong=False) -> Dict[str, str]:
        """
        Create search or editing criteria based on user input.

        Args:
        strong(bool): Boolean flag indicating whether to enforce non-empty values.

        Returns:
        Dict[str, str]: Dictionary representing the search or editing criteria.
        """

        summary_fields = {}
        if not strong:
            print('Значения опциональны. Оставить поле пустым при необходимости.')

        for field in Phonebook.FIELDS:
            while True:
                value = input(f'{field}: ')
                if value:
                    summary_fields[field] = value
                    break
                elif strong and not value:
                    print('Поле нельзя оставить пустым')
                else:
                    break

        return summary_fields
