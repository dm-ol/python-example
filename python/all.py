# Функція all() повертає True, якщо всі елементи заданого ітерованого об’єкта дорівнюють True. Якщо ні, повертається False.

boolean_list = ['True', 'True', 'True']

# Перевіряємо, чи всі елементи дорівнюють True
result = all(boolean_list)
print(result)

# Як функція all() працює зі списками?

# Всі значення дорівнюють True
l = [1, 3, 4, 5]
print(all(l))

# Всі значення дорівнюють False
l = [0, False]
print(all(l))

# Одне зі значень дорівнюює False
l = [1, 3, 4, 0]
print(all(l))

# Одне зі значень дорівнюює True
l = [0, False, 5]
print(all(l))

# Порожній ітерований об'єкт
l = []
print(all(l))

# Як функція all() працює з рядками?

s = "This is good"
print(all(s))

# '0' дорівнює True, оскільки це символ рядка
s = '000'
print(all(s))

s = ''
print(all(s))
