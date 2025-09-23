def find_subsequence(lst, subseq):
    """
    Пошук підпослідовності subseq у списку lst.
    Повертає індекс початку або -1, якщо не знайдено.
    """
    n, m = len(lst), len(subseq)
    for i in range(n - m + 1):
        if lst[i:i+m] == subseq:
            return i
    return -1


def main():
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = user_input.split()

    subseq_input = input(
        "Введіть послідовність елементів для пошуку через пробіл: ")
    subseq = subseq_input.split()

    pos = find_subsequence(lst, subseq)

    if pos != -1:
        print(
            f"Послідовність знайдена, починається з позиції {pos} (нумерація з 0).")
    else:
        print("Послідовність не знайдена.")


if __name__ == "__main__":
    main()
