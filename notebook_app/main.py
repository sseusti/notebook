import inquirer
from inquirer import prompt
from note_manager import Notebook

if __name__ == '__main__':
    username = input("Enter username: ")
    notebook = Notebook(username)

    is_active = True

    while is_active:
        questions = [
            inquirer.List('choice',
                          message='Выберите пункт меню: ',
                          choices=['Показать мои заметки', 'Открыть заметку', 'Добавить заметку', 'Изменить заметку', 'Удалить заметку', 'Выйти'])
        ]

        choice = prompt(questions)['choice']

        if choice == 'Добавить заметку':
            title = input('Введите заголовок: ')
            text = input('Введите текст: ')

            notebook.create_note(title, text)
            print('Заметка успешно добавлена\n')

        elif choice == 'Выйти':
            print('Выход из программы\n')
            is_active = False

        elif choice == 'Показать мои заметки':
            notebook.show_all_notes()

        elif choice == 'Открыть заметку':
            notebook.show_all_notes()
            name = input('Введите id или заголовок заметки: ')
            notebook.open_note(name)

        elif choice == 'Удалить заметку':
            notebook.show_all_notes()
            name = input('Введите id или заголовок заметки: ')
            notebook.remove_note(name)

        elif choice == 'Изменить заметку':
            notebook.show_all_notes()
            name = input('Введите id или заголовок заметки: ')
            new_title = input('Введите новый заголовок или оставьте поле пустым чтобы оставить без изменения: ')
            new_text = input('Введите новый текст или оставьте поле пустым чтобы оставить без изменения: ')
            notebook.change_note(name, new_title, new_text)

