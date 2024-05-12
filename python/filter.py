# Функція filter() вибирає елементи з ітерованого об’єкта (список, кортеж, тощо)
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
