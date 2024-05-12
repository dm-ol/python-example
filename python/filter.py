# Функція filter() вибирає елементи з ітерованого об’єкта (множини, списки, кортежі тощо)
# на основі вихідних даних функції. Функція застосовується до кожного елемента
# ітерованого об’єкта, і якщо вона повертає True, то елемент буде обраний функцією filter().
# Синтаксис функції filter():  filter(function, iterable)

# Повертаємо True, якщо переданий аргумент є парним
def check_even(number):
    if number % 2 == 0:
        return True

    return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Якщо елемент, переданий у функцію check_even(), повертає True, вибираємо його
even_numbers_iterator = filter(check_even, numbers)

# Конвертуємо в список
even_numbers = list(even_numbers_iterator)

print(even_numbers)

# Приклад №1: Робота функції filter()
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# Функція повертає True, якщо елемент є голосною літерою


def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False


filtered_vowels = filter(filter_vowels, letters)

# Конвертуємо в кортеж
vowels = tuple(filtered_vowels)
print(vowels)

# Приклад №2: Використання лямбда-функції всередині функції filter()

numbers = [1, 2, 3, 4, 5, 6, 7]

# Лямбда-функція повертає True для парних чисел
even_numbers_iterator = filter(lambda x: (x % 2 == 0), numbers)

# Конвертуємо в список
even_numbers = list(even_numbers_iterator)

print(even_numbers)
