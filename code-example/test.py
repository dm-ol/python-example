#

id_1 = {112, 114, 116, 118, 115}
id_2 = {112, 114, 116, 118, 115}

print(id_1 == id_2)  # Порівнює значення об'єкта
print(id_1 is id_2)  # Порівнює самі об'єкти
print(112 in id_1)  # Перевіряє наявність в значеннях
print(114 not in id_2)  # Перевіряє відсутність в значеннях
