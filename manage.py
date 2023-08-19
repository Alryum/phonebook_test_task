from phonebook_utils import Phonebook


def main():
    phonebook = Phonebook('phonebook.csv')
    phonebook_list = phonebook.load_phonebook()
    while True:
        print_menu()
        choice = input('Выберите действие: ')
        process_choice(choice, phonebook, phonebook_list)


def print_menu():
    print('1. Вывести записи')
    print('2. Добавить запись')
    print('3. Редактировать запись')
    print('4. Поиск записей')


def process_choice(choice: str, phonebook: Phonebook, phonebook_list):
    if choice == '1':
        phonebook.display_entries(phonebook_list)
    elif choice == '2':
        phonebook.add_entry(phonebook_list)
    elif choice == '3':
        phonebook.edit_entry(phonebook_list)
    elif choice == '4':
        matching_entries = phonebook.search_entries(phonebook_list)
        matching_entries_without_id = matching_entries_without_id = [
            sub_dict for main_dict in matching_entries for sub_dict in main_dict.values()]
        phonebook.display_entries(matching_entries_without_id)
    else:
        print('Некорректный выбор. Пожалуйста, выберите снова.')


if __name__ == "__main__":
    main()
