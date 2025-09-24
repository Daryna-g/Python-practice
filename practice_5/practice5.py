# Словник країн
countries = {
    "Україна": {"площа": 603_500, "населення": 41_000_000, "частина_світу": "Європа"},
    "Єгипет": {"площа": 1_010_000, "населення": 109_000_000, "частина_світу": "Африка"},
    "Китай": {"площа": 9_600_000, "населення": 1_400_000_000, "частина_світу": "Азія"},
    "Бразилія": {"площа": 8_516_000, "населення": 214_000_000, "частина_світу": "Південна Америка"},
    "Нігерія": {"площа": 923_768, "населення": 223_000_000, "частина_світу": "Африка"},
    "Канада": {"площа": 9_985_000, "населення": 39_000_000, "частина_світу": "Північна Америка"},
    "Індія": {"площа": 3_287_000, "населення": 1_417_000_000, "частина_світу": "Азія"},
    "Франція": {"площа": 643_801, "населення": 68_000_000, "частина_світу": "Європа"},
    "Австралія": {"площа": 7_692_000, "населення": 26_000_000, "частина_світу": "Австралія"},
    "ПАР": {"площа": 1_221_037, "населення": 60_000_000, "частина_світу": "Африка"}
}

# --- Функції ---


def print_country(country: str, info: dict):
    print(f"{country}: площа = {info.get('площа')}, населення = {info.get('населення')}, частина світу = {info.get('частина_світу')}")


def show_all(countries_dict):
    for country, info in countries_dict.items():
        print(f"{country}: {info}")


def add_country(countries_dict):
    try:
        name = input("Введіть назву країни: ")
        if name in countries_dict:
            print("Така країна вже існує у словнику.")
            return
        area = int(input("Введіть площу (км²): "))
        population = int(input("Введіть населення: "))
        continent = input("Введіть частину світу: ")
        countries_dict[name] = {
            "площа": area, "населення": population, "частина_світу": continent}
        print("Країну успішно додано!")
    except ValueError:
        print("Помилка: площа та населення повинні бути цілими числами.")


def delete_country(countries_dict):
    name = input("Введіть назву країни для видалення: ")
    try:
        del countries_dict[name]
        print("Країну успішно видалено!")
    except KeyError:
        print("Помилка: такої країни немає у словнику.")


UKR_ALPHABET = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
ALPH_INDEX = {ch: i for i, ch in enumerate(UKR_ALPHABET)}


def ukr_sort_key(s: str):
    s = s.strip().upper()
    key = []
    for ch in s:
        if ch in ALPH_INDEX:
            key.append(ALPH_INDEX[ch])
        else:
            key.append(len(UKR_ALPHABET) + ord(ch))
    return key


def show_sorted(countries_dict):
    if not countries_dict:
        print("Словник пустий.")
        return
    for country in sorted(countries_dict.keys(), key=ukr_sort_key):
        print_country(country, countries_dict[country])


def find_asia_africa(countries_dict):
    result = [c for c, info in countries_dict.items(
    ) if info["частина_світу"] in ("Африка", "Азія")]
    if result:
        print("Країни, що знаходяться в Африці або Азії:")
        print(", ".join(result))
    else:
        print("Країн в Африці чи Азії немає.")

# --- Основна програма ---


def main():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Вивести всі країни")
        print("2. Додати країну")
        print("3. Видалити країну")
        print("4. Вивести країни за алфавітом")
        print("5. Пошук країн в Африці та Азії")
        print("0. Вихід")

        choice = input("Ваш вибір: ")
        if choice == "1":
            show_all(countries)
        elif choice == "2":
            add_country(countries)
        elif choice == "3":
            delete_country(countries)
        elif choice == "4":
            show_sorted(countries)
        elif choice == "5":
            find_asia_africa(countries)
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
