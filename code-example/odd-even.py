# Програма, яка читає послідовність чисел
# і підраховує, скільки чисел парних і скільки непарних.
# Програма завершується, коли вводиться нуль.
odd_numbers = 0
even_numbers = 0
 
# Прочитайте перше число.
try:
    number = int(input("Введіть число або 0, щоб зупинити: "))
except ValueError:
    print("Помилка: Будь ласка введіть числове значення.")
    quit() 
# 0 завершує виконання.
while number != 0:
    # Перевірте, чи число непарне.
    if number % 2 == 1:
        # Збільшити odd_numbers лічильник.
        odd_numbers = odd_numbers + 1 # також можна odd_numbers += 1
    else:
        # Збільшити even_numbers лічильник.
        even_numbers = even_numbers + 1 # також можна even_numbers += 1
    # Прочитайте наступне число.
    try:
        number = int(input("Введіть число або 0, щоб зупинити: "))
    except ValueError:
        print("Помилка: Будь ласка введіть числове значення.")
        continue
# Роздрукувати результати.
print("Кількість непарних чисел:", odd_numbers)
print("Кількість парних чисел:", even_numbers)
 
