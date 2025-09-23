def analyze_text(text: str):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    text = text.lower()

    letters = [ch for ch in text if ch.isalpha()]

    set_vowels = set(ch for ch in letters if ch in vowels)
    set_consonants = set(ch for ch in letters if ch not in vowels)

    count_vowels = sum(1 for ch in letters if ch in vowels)
    count_consonants = sum(1 for ch in letters if ch not in vowels)

    print("Множина голосних у тексті:", set_vowels)
    print("Множина приголосних у тексті:", set_consonants)

    if count_vowels > count_consonants:
        print(f"Голосних більше ({count_vowels} > {count_consonants})")
    elif count_consonants > count_vowels:
        print(f"Приголосних більше ({count_consonants} > {count_vowels})")
    else:
        print(f"Кількість голосних і приголосних однакова ({count_vowels})")


text = input("Введіть текст (латиниця + цифри): ")
analyze_text(text)
