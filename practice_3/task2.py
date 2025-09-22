word = input("Введіть слово: ")

letters_count = {}

for letter in word:
    if letter.isalpha():
        letters_count[letter] = letters_count.get(letter, 0) + 1

duplicates = [letter for letter, count in letters_count.items() if count > 1]

if duplicates:
    print("Повторювані літери:", ", ".join(duplicates))
else:
    print("У слові немає повторюваних літер.")
