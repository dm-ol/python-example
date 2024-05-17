# Функція iter() повертає ітератор для вказаного аргументу.
# Синтаксис функції iter(): iter(object, sentinel)

# Список телефонів
phones = ['apple', 'samsung', 'oneplus']
phones_iter = iter(phones)

print(next(phones_iter))
print(next(phones_iter))
print(next(phones_iter))

# Приклад №1: Функція iter() в Python

# Список голосних
vowels = ["a", "e", "i", "o", "u"]

# Функція iter() зі списком голосних
vowels_iter = iter(vowels)

print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
