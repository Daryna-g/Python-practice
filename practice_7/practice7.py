import re


def create_file(filename):
    """Створює текстовий файл TF4_1 із рядками тексту."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Я ішов від озерця.\n")
            f.write("Ти сказала мені: “Будь здоров!\n")
            f.write("Будь здоров, ти мій любий юначе!..”\n")
            f.write("Ах, а серце і досі ще плаче.\n")
            f.write("Я ішов від озерця…\n")
        print(f"Файл {filename} створено.")
    except Exception as e:
        print(f"Помилка створення файлу {filename}: {e}")


def analyze_words(input_file, output_file):
    """Зчитує TF4_1, аналізує довжину слів і записує результати в TF4_2."""
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")
        return
    except Exception as e:
        print(f"Помилка читання файлу {input_file}: {e}")
        return

    words = re.findall(r"\b\w+\b", text, re.UNICODE)

    # Статистика по довжинах слів
    word_lengths = {}
    for word in words:
        length = len(word)
        if length <= 16:
            word_lengths[length] = word_lengths.get(length, 0) + 1

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for length in sorted(word_lengths.keys()):
                f.write(f"Слова довжини {length}: {word_lengths[length]}\n")
        print(f"Результати записано у файл {output_file}.")
    except Exception as e:
        print(f"Помилка запису у файл {output_file}: {e}")


def print_file(filename):
    """Друкує вміст файлу TF4_2."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except Exception as e:
        print(f"Помилка читання файлу {filename}: {e}")


file1 = "TF4_1.txt"
file2 = "TF4_2.txt"

create_file(file1)
analyze_words(file1, file2)
print("\nВміст файлу TF4_2:")
print_file(file2)
