import math

# 1) Функція для обчислення z = 1 / sqrt(m + 2)


def calc_z(m):
    if m + 2 <= 0:
        return "Помилка: підкореневий вираз (m + 2) повинен бути додатнім!"
    z = 1 / math.sqrt(m + 2)
    return z

# 2) Функція для обчислення сумарного шляху спортсмена


def total_distance(n):
    distance = 10  # відстань у перший день
    total = 0
    for i in range(n):
        total += distance
        distance *= 1.1  # збільшення на 10%
    return total


# --- Основна програма ---
# Виклик першої функції
m = float(input("Введіть число m: "))
print("Результат z =", calc_z(m))

# Виклик другої функції
n = int(input("Введіть кількість днів тренування n: "))
if n <= 0:
    print("Помилка: n повинно бути додатним числом!")
else:
    print(f"Сумарний шлях за {n} днів = {total_distance(n):.2f} км")
