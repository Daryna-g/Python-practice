# --- словник ---
students = {
    "101": {
        "група": "КН-21",
        "ПІБ": "Іваненко Петро Олександрович",
        "курс": 2,
        "успішність": {
            "Математика": 90,
            "Програмування": 85,
            "Англійська": 78
        }
    },
    "102": {
        "група": "КН-21",
        "ПІБ": "Шевченко Марія Іванівна",
        "курс": 2,
        "успішність": {
            "Математика": 95,
            "Програмування": 92,
            "Англійська": 88
        }
    }
}

# ---- функції ---


def add_student(students_dict):
    """Додавання нового студента у словник"""
    student_id = input("Введіть ID (номер залікової книжки): ")
    if student_id in students_dict:
        print("Студент з таким ID вже існує!")
        return

    group = input("Введіть номер групи: ")
    pib = input("Введіть ПІБ студента: ")
    try:
        course = int(input("Введіть курс (число): "))
    except ValueError:
        print("Помилка: курс має бути числом!")
        return

    marks = {}
    while True:
        subject = input("Введіть назву предмета (або Enter для завершення): ")
        if subject == "":
            break
        try:
            mark = int(input(f"Введіть оцінку з предмета {subject}: "))
            marks[subject] = mark
        except ValueError:
            print("Оцінка має бути числом!")

    students_dict[student_id] = {
        "група": group,
        "ПІБ": pib,
        "курс": course,
        "успішність": marks
    }
    print("Студента успішно додано!")


def show_sorted(students_dict):
    """Вивести студентів, відсортованих за прізвищем"""
    sorted_students = sorted(students_dict.items(),
                             key=lambda x: x[1]["ПІБ"].split()[0])
    for student_id, data in sorted_students:
        print(
            f"{student_id}: {data['ПІБ']} (група {data['група']}, курс {data['курс']})")


def delete_student(students_dict):
    """Видалення студента за його ID"""
    student_id = input("Введіть ID студента, якого потрібно видалити: ")
    if student_id in students_dict:
        removed = students_dict.pop(student_id)
        print(f"Студента {removed['ПІБ']} успішно видалено.")
    else:
        print("Студента з таким ID немає у словнику!")

# --- основна програма ---


def main():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Додати студента")
        print("2. Вивести студентів за прізвищем")
        print("3. Видалити студента")
        print("0. Вихід")

        choice = input("Ваш вибір: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_sorted(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "0":
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
