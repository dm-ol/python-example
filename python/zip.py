# Функція zip() приймає ітеровані об’єкти, об’єднує їх у кортеж та повертає.
# Це можуть бути вбудовані ітеровані об’єкти (наприклад: список, рядок, словник)
# або користувацькі ітеровані об’єкти.

languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3.11, 6.5]

result = list(zip(languages, versions))  # конвертація в список
result_2 = dict(zip(languages, versions))  # конвертація в словник
print(result)
print(result_2)

# Припустимо, у функцію zip() передані два ітеровані об’єкти: перший ітерований
# об’єкт містить три елементи, а другий — п’ять елементів. Тоді повернений ітератор
# міститиме три кортежі, оскільки ітератор зупиняється, коли закінчується найкоротший ітерований об’єкт.

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Зверніть увагу, що довжина numbersList і numbers_tuple різна
result = zip(numbersList, numbers_tuple)

# Конвертуємо у множину
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Конвертуємо у множину
result_set = set(result)
print(result_set)


# “Розпакування” значень за допомогою функції zip()

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v = zip(*result_list)
print('c =', c)
print('v =', v)
