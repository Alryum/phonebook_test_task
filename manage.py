import phonebook_utils


def main():
    phonebook = phonebook_utils.load_phonebook()

    while True:
        print('1. Вывести записи')
        print('2. Добавить запись')
        print('3. Редактировать запись')
        print('4. Поиск записей')

        choice = input('Выберите действие: ')

        if choice == '1':
            phonebook_utils.display_entries(phonebook)
        elif choice == '2':
            phonebook_utils.add_entry(phonebook)
        elif choice == '3':
            first_name = input("Введите имя для редактирования: ")
            last_name = input("Введите фамилию для редактирования: ")
            phonebook_utils.edit_entry(phonebook, first_name, last_name)
        elif choice == '4':
            search_criteria = phonebook_utils.create_search_criteria()
            matching_entries = phonebook_utils.search_entries(phonebook, search_criteria)
            phonebook_utils.display_entries(matching_entries)
        else:
            print('Некорректный выбор. Пожалуйста, выберите снова.')


if __name__ == "__main__":
    main()
