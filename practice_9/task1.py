import csv


def main():
    # файл з порталу World Bank
    input_file = "API_NY.GDP.PCAP.CD_DS2_en_csv_v2_1092359.csv"
    output_file = "gdp_filtered.csv"

    try:
        with open(input_file, mode="r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            rows = list(reader)
    except FileNotFoundError:
        print(f"Помилка: файл '{input_file}' не знайдено.")
        return
    except Exception as e:
        print(f"Сталася помилка під час відкриття файлу: {e}")
        return

    header_index = None
    for i, row in enumerate(rows):
        if len(row) > 0 and row[0].strip() == "Country Name":
            header_index = i
            break

    if header_index is None:
        print("Не знайдено заголовок 'Country Name' у файлі.")
        return

    header = rows[header_index]
    data_rows = rows[header_index + 1:]

    # Знайдемо індекс колонки за 2016 рік
    try:
        year_index = header.index("2016")
    except ValueError:
        print("У файлі немає даних за 2016 рік.")
        return

    # Створюємо список із даними по країнах
    gdp_data = []
    for row in data_rows:
        if len(row) <= year_index:
            continue
        country = row[0]
        value = row[year_index]
        if value:
            try:
                gdp = float(value)
                gdp_data.append((country, gdp))
            except ValueError:
                continue

    print("Дані GDP per capita (current US$) за 2016 рік:")
    for country, gdp in gdp_data:
        print(f"{country}: {gdp}")

    try:
        threshold = float(
            input("\nВведіть порогове значення GDP per capita: "))
    except ValueError:
        print("Помилка: потрібно ввести число.")
        return

    # Фільтруємо дані
    filtered_data = [(c, g) for c, g in gdp_data if g > threshold]

    # Записуємо у новий CSV файл
    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Country", "GDP per capita (2016, US$)"])
            writer.writerows(filtered_data)
        print(f"\nРезультати збережено у файл '{output_file}'.")
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")


if __name__ == "__main__":
    main()
