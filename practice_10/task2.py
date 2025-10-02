import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("API_SE.PRM.UNER_DS2_en_csv_v2_1014134.csv", skiprows=4)

years = [str(y) for y in range(2000, 2021)]

indicator = "Children out of school, primary"
country1 = "Ukraine"
country2 = "Poland"

# Фільтруємо дані
df_country1 = data[data["Country Name"] == country1]
df_country2 = data[data["Country Name"] == country2]

values_country1 = df_country1[years].fillna(0).values.flatten()
values_country2 = df_country2[years].fillna(0).values.flatten()

# Перевірка, чи дані існують
if len(values_country1) == 0 or len(values_country2) == 0:
    print("Дані для обраних країн відсутні або назви введені некоректно.")
else:
    # Лінійний графік
    plt.figure(figsize=(10, 6))
    plt.plot(years, values_country1, label=country1, color="blue", linewidth=2)
    plt.plot(years, values_country2, label=country2, color="red", linewidth=2)
    plt.xlabel("Рік")
    plt.ylabel("Кількість дітей")
    plt.title(f"Динаміка '{indicator}' (2000–2020)")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

# Стовпчикова діаграма для користувача
user_country = input("Введіть назву країни для стовпчикової діаграми: ")
df_user = data[data["Country Name"] == user_country]
values_user = df_user[years].fillna(0).values.flatten()

if len(values_user) == 0:
    print(
        f"Дані для країни '{user_country}' відсутні або назва введена некоректно.")
else:
    plt.figure(figsize=(10, 6))
    plt.bar(years, values_user, color="green")
    plt.xlabel("Рік")
    plt.ylabel("Кількість дітей")
    plt.title(
        f"Стовпчикова діаграма: '{indicator}' для {user_country} (2000–2020)")
    plt.xticks(rotation=45)
    plt.show()
