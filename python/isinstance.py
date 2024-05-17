# Функція isinstance() перевіряє, чи є об’єкт (перший аргумент) екземпляром/об’єктом
# або підкласом класу (другий аргумент). Синтаксис функції isinstance(): isinstance(object, classinfo)

numbers = [1, 2, 3, 4, 2, 5]

# Перевіряємо, чи є numbers об'єктом класу list
result = isinstance(numbers, list)
print(result)
