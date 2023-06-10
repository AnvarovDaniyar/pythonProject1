import json
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    notes = []
    with open(NOTES_FILE, "r") as file:
        notes = json.load(file)
    return notes

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().isoformat()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена.")

def list_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело заметки: {note['body']}")
        print(f"Дата/время создания: {note['timestamp']}")
        print("----------------------")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    found = False
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            timestamp = datetime.datetime.now().isoformat()
            note["title"] = title
            note["body"] = body
            note["timestamp"] = timestamp
            found = True
            break
    if found:
        save_notes(notes)
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка не найдена.")

def filter_notes_by_date():
    date_str = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        filtered_notes = [note for note in notes if datetime.datetime.fromisoformat(note["timestamp"]).date() == date]
        if filtered_notes:
            print(f"Заметки на дату {date_str}:")
            for note in filtered_notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Тело заметки: {note['body']}")
                print(f"Дата/время создания: {note['timestamp']}")
                print("----------------------")
        else:
            print("Нет заметок на указанную дату.")
    except ValueError:
        print("Неверный формат даты.")

def main():
    global notes
    try:
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    while True:
        command = input("Введите команду (add, list, edit, delete, filter, exit): ")
        if command == "add":
            add_note()
        elif command == "list":
            list_notes()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "filter":
            filter_notes_by_date()
        elif command == "exit":
            break
        else:
            print("Неверная команда.")

if __name__ == "__main__":
    main()