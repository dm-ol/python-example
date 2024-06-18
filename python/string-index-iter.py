# Наприклад, якщо ви хочете отримати доступ до будь-якого символу рядка, ви можете зробити це за допомогою індексування

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()


# Ітерація рядків теж працює.

# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()


# Метод index () (це метод, а не функція) шукає послідовність з початку,
# щоб знайти перший елемент значення, указаного в його аргументі .

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))
