#

id_1 = {112, 114, 116, 118, 115}
id_2 = {112, 114, 116, 118, 115}
id_3 = [2]

print(id_1 == id_2)  # Порівнює значення об'єкта
print(id_1 is id_2)  # Порівнює самі об'єкти
print(112 in id_1)  # Перевіряє наявність в значеннях
print(114 not in id_2)  # Перевіряє відсутність в значеннях


# Приклад використання and + or
id_3 and print("List is not empty") or print("List is empty")
