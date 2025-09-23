def insert_element(lst, element, position):
    """
    Вставляє елемент у список у вказану позицію.
    Якщо позиція більша за довжину списку – елемент додається в кінець.
    """
    if position < 0:
        position = 0
    elif position > len(lst):
        position = len(lst)
    lst.insert(position, element)
    return lst


def main():
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = user_input.split()

    element = input("Введіть елемент, який потрібно вставити: ")

    position = int(input("Введіть позицію для вставки (починаючи з 0): "))

    result = insert_element(lst, element, position)

    print("Список після вставки:", result)


if __name__ == "__main__":
    main()
