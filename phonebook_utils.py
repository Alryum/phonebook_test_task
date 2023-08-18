import csv
import locale

phonebook_file = "phonebook.csv"
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def load_phonebook() -> list:
    with open(phonebook_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        return sorted(list(reader), key=lambda x: x["Фамилия"])


def save_phonebook(entries):
    with open(phonebook_file, "w", newline="") as file:
        fieldnames = ["Фамилия", "Имя", "Отчество",
                      "Организация", "Рабочий телефон", "Личный телефон"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)


def display_entries(entries):
    print(f"{'Фамилия':<15} {'Имя':<15} {'Отчество':<15} {'Организация':<15} {'Рабочий телефон':<15} {'Личный телефон':<15}")
    print('-' * 90)
    for row in entries:
        print(f"{row['Фамилия']:<15} {row['Имя']:<15} {row['Отчество']:<15} {row['Организация']:<15} {row['Рабочий телефон']:<15} {row['Личный телефон']:<15}")
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
