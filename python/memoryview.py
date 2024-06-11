# Функція memoryview() в Python повертає об’єкт представлення пам’яті із вказаного об’єкта.
# Представлення пам’яті — це безпечний спосіб розкрити буферний протокол в Python,
# який дозволяє отримати доступ до внутрішніх буферів об’єкта шляхом створення об’єкта представлення пам’яті.

x = memoryview(b"Hello")

print(x)

# Повертаємо Unicode першого символу
print(x[0])

# Повертаємо Unicode другого символу
print(x[1])

# Приклад №1: Як працює функція memoryview() у Python?

# Випадковий байтовий масив
random_byte_array = bytearray('ABC', 'utf-8')

mv = memoryview(random_byte_array)

# Отримуємо доступ до представлення  пам'яті за нульовим індексом
print(mv[0])

# Створюємо байт з представлення пам'яті
print(bytes(mv[0:2]))

# Створюємо список з представлення пам'яті
print(list(mv[0:3]))

# Приклад №2: Зміна внутрішніх даних за допомогою представлення пам’яті

# Випадковий байтовий масив
random_byte_array = bytearray('ABC', 'utf-8')
print('Before updation:', random_byte_array)

mv = memoryview(random_byte_array)

# Оновлюємо перший індекс mv на Z
mv[1] = 90
print('After updation:', random_byte_array)
