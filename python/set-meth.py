# Додавання елемента до множини. Метод add() використовується для додавання елемента до множини.

numbers = {21, 34, 54, 12}

print('Initial Set:', numbers)

# Використання методу add()
numbers.add(32)  # Тут add() додає значення 32 до нашої множини.

print('Updated Set:', numbers)

# Оновлення множини. Метод update() використовується для оновлення множини елементів інших типів даних.

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['Apple', 'Google', 'Samsung']

# Тут всі унікальні елементи tech_companies додаються до множини companies.
companies.update(tech_companies)

print(companies)

# Видалення елемента з множини. Метод discard() використовується для видалення зазначеного елемента з множини.

languages = {'Swift', 'Java', 'Python'}

print('Initial Set:', languages)

# Видалення 'Java' з множини
removedValue = languages.discard('Java')

print('Set after remove():', languages)

# Визначення кількості елементів множини. Метод len() використовується для визначення кількості елементів, присутніх у множині.

even_numbers = {2, 4, 6, 8}
print('Set:', even_numbers)

print('Total Elements:', len(even_numbers))

# Об’єднання множин. Об’єднання двох множин A та B включає всі елементи множин A та B.

A = {1, 3, 5}  # Перша множина

B = {0, 2, 4}  # Друга множина

print('Union using |:', A | B)  # Виконання операції об'єднання за допомогою |

# Виконання операції об'єднання за допомогою union()
print('Union using union():', A.union(B))


# Перетин множин. Перетин двох множин A і B включає загальні елементи між множинами A та B.

A = {1, 3, 5}  # Перша множина

B = {1, 2, 3}  # Друга множина

# Виконання операції перетину за допомогою &
print('Intersection using &:', A & B)

# Виконання операції перетину за допомогою intersection()
print('Intersection using intersection():', A.intersection(B))


# Різниця множин. Різниця між двома множинами A і B включає елементи множини A, яких немає в множині B.

A = {2, 3, 5}  # Перша множина

B = {1, 2, 6}  # Друга множина

# Виконання операції різниці за допомогою -
print('Difference using -:', A - B)

# Виконання операції різниці за допомогою difference()
print('Difference using difference():', A.difference(B))


# Симетрична різниця множин. Симетрична різниця двох множин A і B включає всі елементи A і B без спільних елементів.

A = {2, 3, 5}  # Перша множина

B = {1, 2, 6}  # Друга множина

# Виконання операції симетричної різниці за допомогою &
print('using ^:', A ^ B)

# Виконання операції симетричної різниці за допомогою symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))


# Перевірка, чи є дві множини рівними.

A = {1, 3, 5}  # Перша множина

B = {3, 5, 1}  # Друга множина

# Перевіряємо, чи рівні дві множини
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')
