# Функція iter() повертає ітератор для вказаного аргументу.
# Синтаксис функції iter(): iter(object, sentinel)

# Список голосних
phones = ['apple', 'samsung', 'oneplus']
phones_iter = iter(phones)

print(next(phones_iter))
print(next(phones_iter))
print(next(phones_iter))
