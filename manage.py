import phonebook_utils


def main():
    phonebook = phonebook_utils.load_phonebook()
    while True:
        print_menu()
        choice = input('Выберите действие: ')
        process_choice(choice, phonebook)


def print_menu():
    print('1. Вывести записи')
    print('2. Добавить запись')
    print('3. Редактировать запись')
    print('4. Поиск записей')


def process_choice(choice, phonebook):
    if choice == '1':
        phonebook_utils.display_entries(phonebook)
    elif choice == '2':
        phonebook_utils.add_entry(phonebook)
    elif choice == '3':
        phonebook_utils.edit_entry(phonebook)
    elif choice == '4':
        matching_entries = phonebook_utils.search_entries(phonebook)
        matching_entries_without_id = matching_entries_without_id = [
            sub_dict for main_dict in matching_entries for sub_dict in main_dict.values()]
        phonebook_utils.display_entries(matching_entries_without_id)
    else:
        print('Некорректный выбор. Пожалуйста, выберите снова.')


if __name__ == "__main__":
    main()
