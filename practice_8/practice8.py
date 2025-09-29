def create_student_file(filename):
    """Створює файл з прізвищем та питанням для наступного студента."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Прізвище: Гичка\n")
            f.write(
                "Питання: Що таке список (list) у Python та які основні операції з ним можна виконувати?\n")
        print(f"Файл {filename} успішно створено.")
    except Exception as e:
        print(f"Помилка створення файлу {filename}: {e}")


filename = "students.txt"
create_student_file(filename)
