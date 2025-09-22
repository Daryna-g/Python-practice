sentence = input("Введіть речення: ")

words = sentence.split()

# Лічильник слів на "н"
count = 0

for word in words:
    if word.lower().startswith("н"):
        count += 1

print("Кількість слів, які починаються з літери 'н':", count)
