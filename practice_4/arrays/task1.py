def main():
    n = int(input("Введіть довжину масиву: "))

    # Введення елементів масиву
    arr = []
    print(f"Введіть {n} дійсних чисел:")
    for i in range(n):
        num = float(input(f"Елемент {i+1}: "))
        arr.append(num)

    negative_elements = [x for x in arr if x < 0]

    # Перевірка, чи є від’ємні елементи
    if negative_elements:
        avg = sum(negative_elements) / len(negative_elements)
        print(f"Середнє арифметичне від’ємних елементів: {avg}")
    else:
        print("У масиві немає від’ємних елементів.")


if __name__ == "__main__":
    main()
