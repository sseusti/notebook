import json
import datetime


class Notebook:
    FORMAT_DATA = "%d/%m/%Y"
    FORMAT_TIME = "%H:%M %A"

    def __init__(self, username):
        self.username = username
        self.file = f"data/{username}.json"
        self.current_id = len(self._load())

        data = self._load()
        self._dump(data)

    def _load(self):
        try:
            with open(self.file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _dump(self, data):
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=4)

    def _find_note(self, name):
        if name.isalnum():
            filter_name = 'id'
            name = int(name)
        else:
            filter_name = 'title'

        notes = self._load()
        for note in notes:
            if note[filter_name] == name:
                return note
        return None

    def create_note(self, title, text):
        data = self._load()

        dt = datetime.datetime.now()
        time = dt.strftime(self.FORMAT_TIME)
        date = dt.strftime(self.FORMAT_DATA)

        new_note = {
            'id': self.current_id,
            'date': date,
            'title': title,
            'text': text,
            'time': time
        }

        data.append(new_note)
        self._dump(data)
        self.current_id += 1

    def show_all_notes(self):
        notes = self._load()

        if len(notes) != 0:
            print('id | Заголовок')
            print('---+----------')
            for note in notes:
                print(f" {note['id']} | {note['title']}")
            print('\n')
        else:
            print(f'Похоже у {self.username} еще нет заметок\n')

    def open_note(self, name):
        note = self._find_note(name)

        print(f"Заметка от {note['date']}\n"
              f"\033[1m{note['title']}\033[0m\n"
              f"{note['text']}\n"
              f"{note['time']}\n")

    def remove_note(self, name):
        note = self._find_note(name)
        notes = self._load()

        notes.remove(note)
        self._dump(notes)
        print(f"Заметка {note['id']} удалена\n")

    def change_note(self, name, new_title, new_text):
        notes = self._load()
        note = self._find_note(name)
        index_to_change = notes.index(note)

        dt = datetime.datetime.now()
        time = dt.strftime(self.FORMAT_TIME)
        date = dt.strftime(self.FORMAT_DATA)

        new_note = {
            'id': note['id'],
            'date': date,
            'title': new_title if new_title  != '' else note['title'],
            'text': new_text if new_text != '' else note['text'],
            'time': time
        }

        notes[index_to_change] = new_note
        self._dump(notes)
        print('Заметка успешно изменена\n')

