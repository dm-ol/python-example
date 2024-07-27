# Функція any() повертає True, якщо хоча б один з елементів ітерованого об’єкта дорівнює True.
# Функція any() приймає ітерований об’єкт (список, рядок, словник і т.д.) в Python.

boolean_list = ['True', 'False', 'True']

# Перевірка, чи дорівнює елемент True
result = any(boolean_list)
print(result)


# Використання функції any() зі списками в Python

# True, оскільки елементи 1,3 та 4 дорівнюють True
l = [1, 3, 4, 0]
print(any(l))

# False, оскільки обидва елементи дорівнюють False
l = [0, False]
print(any(l))

# True, оскільки 5 дорівнює True
l = [0, False, 5]
print(any(l))

# False, оскільки ітерований об'єкт порожній
l = []
print(any(l))


# Використання функції any() з рядками в Python

# Всі елементи дорівнюють True
s = "This is good"
print(any(s))

# Значення 0 дорівнює False, але тут '0' - це символ рядка, тому він дорівнює True
s = '000'
print(any(s))

# False, оскільки ітерований об'єкт порожній
s = ''
print(any(s))


# Використання функції any() зі словниками в Python

# 0 дорівнює False
d = {0: 'False'}
print(any(d))

# 1 дорівнює True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 та False дорівнюють False
d = {0: 'False', False: 0}
print(any(d))

# Ітерований об'єкт порожній
d = {}
print(any(d))

# '0' дорівнює True
d = {'0': 'False'}
print(any(d))
