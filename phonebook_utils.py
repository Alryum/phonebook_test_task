import csv

phonebook_file = "phonebook.csv"


def load_phonebook():
    with open(phonebook_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_phonebook(entries):
    with open(phonebook_file, "w", newline="") as file:
        fieldnames = ["Фамилия", "Имя", "Отчество",
                      "Организация", "Рабочий телефон", "Личный телефон"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)


def display_entries(entries):
    for entry in entries:
        print(entry)
    input('Нажмите для продолжения...')


def add_entry(entries):
    entry = {
        "Фамилия": input("Введите фамилию: "),
        "Имя": input("Введите имя: "),
        "Отчество": input("Введите отчество: "),
        "Организация": input("Введите название организации: "),
        "Рабочий телефон": input("Введите рабочий телефон: "),
        "Личный телефон": input("Введите личный телефон: "),
    }
    entries.append(entry)
    save_phonebook(entries)


def edit_entry(entries):
    # Логика редактирования записи
    pass


def search_entries(entries):
    # Логика поиска записей
    pass
