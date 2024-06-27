# Заморожена множина (англ. “frozen set”) — це просто незмінна версія множини в Python.
# Хоча елементи звичайної множини можна змінити у будь-який час, елементи замороженої
# множини залишаються незмінними після створення. Завдяки цьому заморожені множини можуть
# бути використані як ключі в словнику або як елементи іншої множини.
# Але як і множини, вони не впорядковані (елемент можна поставити в будь-який індекс).

# Робота функції frozenset() в Python

# Кортеж голосних літер
vowels = ('a', 'e', 'i', 'o', 'u')

frSet = frozenset(vowels)
print('The frozen set is:', frSet)
print('The empty frozen set is:', frozenset())

# Заморожені множини - незмінні
frSet.add('v')

# Функція frozenset() зі словником

# Випадковий словник
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)

# Операції над frozenset
# Як звичайні множини, незмінна множина виконує різні операції як копіювання, різниця, перетин, симетрична різниця та об’єднання.

# Заморожені множини.
# Ініціалізуємо A та B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# Копіюємо заморожену множину
C = A.copy()
print(C)

# Об'єднання
print(A.union(B))

# Перетин
print(A.intersection(B))

# Різниця
print(A.difference(B))

# Симетрична різниця
print(A.symmetric_difference(B))

# Заморожені множини.
# Ініціалізуємо A, B та C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# Метод isdisjoint()
print(A.isdisjoint(C))

# Метод issubset()
print(C.issubset(B))

# Метод issuperset()
print(B.issuperset(C))
