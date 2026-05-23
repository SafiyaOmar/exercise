import sqlite3


conn = sqlite3.connect("hostel.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    room_number INTEGER NOT NULL
)
""")


def add_student(name, room_number):
    cursor.execute("INSERT INTO students (name, room_number) VALUES (?, ?)", (name, room_number))
    conn.commit()
    print(f"Mwanafunzi {name} ameongezwa kwenye chumba {room_number}.")


def show_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("Orodha ya wanafunzi:")
    for student in students:
        print(f"ID: {student[0]}, Jina: {student[1]}, Chumba: {student[2]}")


def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Mwanafunzi mwenye ID {student_id} ameondolewa.")


while True:
    print("\n--- Hostel Management System ---")
    print("1. Ongeza mwanafunzi")
    print("2. Onyesha wanafunzi")
    print("3. Futa mwanafunzi")
    print("4. Exit")

    choice = input("Chagua namba: ")

    if choice == "1":
        name = input("Ingiza jina la mwanafunzi: ")
        room = int(input("Ingiza namba ya chumba: "))
        add_student(name, room)
    elif choice == "2":
        show_students()
    elif choice == "3":
        student_id = int(input("Ingiza ID ya mwanafunzi: "))
        delete_student(student_id)
    elif choice == "4":
        print("Kutoka kwenye mfumo...")
        break
    else:
        print("Chaguo batili, tafadhali jaribu tena.")
