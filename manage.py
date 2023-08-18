import phonebook_utils


def main():
    phonebook = phonebook_utils.load_phonebook()

    while True:
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")

        choice = input("Выберите действие: ")

        if choice == "1":
            phonebook_utils.display_entries(phonebook)
        elif choice == "2":
            phonebook_utils.add_entry(phonebook)
        elif choice == "3":
            phonebook_utils.edit_entry(phonebook)
        elif choice == "4":
            phonebook_utils.search_entries(phonebook)
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    main()
