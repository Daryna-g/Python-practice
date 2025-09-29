import json
import os

DATA_FILE = "countries.json"
RESULT_FILE = "africa_asia.json"


def load_data():
    """Завантаження даних із JSON або створення нового файлу."""
    if not os.path.exists(DATA_FILE):
        data = [
            {"name": "Україна", "area": 603700,
                "population": 41000000, "continent": "Європа"},
            {"name": "Єгипет", "area": 1002450,
                "population": 104000000, "continent": "Африка"},
            {"name": "Нігерія", "area": 923769,
                "population": 206000000, "continent": "Африка"},
            {"name": "Китай", "area": 9597000,
                "population": 1400000000, "continent": "Азія"},
            {"name": "Індія", "area": 3287000,
                "population": 1380000000, "continent": "Азія"},
            {"name": "Канада", "area": 9985000,
                "population": 38000000, "continent": "Америка"},
            {"name": "Бразилія", "area": 8516000,
                "population": 213000000, "continent": "Америка"},
            {"name": "Німеччина", "area": 357000,
                "population": 83000000, "continent": "Європа"},
            {"name": "Японія", "area": 377975,
                "population": 126000000, "continent": "Азія"},
            {"name": "ПАР", "area": 1219090,
                "population": 60000000, "continent": "Африка"}
        ]
        save_data(data)
    else:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    return data


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def display_data(data):
    print(json.dumps(data, ensure_ascii=False, indent=4))


def add_country(data):
    name = input("Назва країни: ")
    try:
        area = int(input("Площа: "))
        population = int(input("Населення: "))
    except ValueError:
        print("Помилка: площа та населення мають бути числами.")
        return data
    continent = input("Частина світу: ")

    data.append({"name": name, "area": area,
                "population": population, "continent": continent})
    save_data(data)
    print("Країну додано!")
    return data


def delete_country(data):
    name = input("Введіть назву країни для видалення: ")
    new_data = [c for c in data if c["name"].lower() != name.lower()]
    if len(new_data) != len(data):
        save_data(new_data)
        print(f"Країну '{name}' видалено.")
    else:
        print("Країну не знайдено.")
    return new_data


def search_data(data):
    """Пошук у JSON за одним із полів."""
    field = input(
        "Виберіть поле для пошуку (name, area, population, continent): ")
    value = input("Введіть значення для пошуку: ")

    results = []
    for country in data:
        if str(country.get(field, "")).lower() == value.lower():
            results.append(country)

    if results:
        print("Знайдено записи:")
        print(json.dumps(results, ensure_ascii=False, indent=4))
    else:
        print("Нічого не знайдено.")


def africa_asia_task(data):
    """Знайти країни в Африці або Азії та зберегти їх у новий JSON."""
    filtered = [c for c in data if c["continent"].lower() in [
        "африка", "азія"]]

    if filtered:
        print("Країни з Африки або Азії:")
        for c in filtered:
            print(c["name"])
        with open(RESULT_FILE, "w", encoding="utf-8") as f:
            json.dump(filtered, f, ensure_ascii=False, indent=4)
        print(f"Результати збережено у файл '{RESULT_FILE}'")
    else:
        print("Країн з Африки чи Азії немає.")


def menu():
    data = load_data()
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показати всі країни")
        print("2. Додати країну")
        print("3. Видалити країну")
        print("4. Пошук країни")
        print("5. Країни, що знаходяться в Африці/Азії)")
        print("0. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            display_data(data)
        elif choice == "2":
            data = add_country(data)
        elif choice == "3":
            data = delete_country(data)
        elif choice == "4":
            search_data(data)
        elif choice == "5":
            africa_asia_task(data)
        elif choice == "0":
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    menu()
