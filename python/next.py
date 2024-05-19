# Функція next() повертає наступний елемент ітератора.
# Синтаксис функції next(): next(iterator, default)

marks = [65, 71, 68, 74, 61]
 
# Конвертуємо список в ітератор
iterator_marks = iter(marks)
 
# Наступний елемент є першим елементом
marks_1 = next(iterator_marks)
print(marks_1)
 
# Шукаємо наступний елемент, який є другим елементом
marks_2 = next(iterator_marks)
print(marks_2)

# Приклад №1: Отримання наступного елемента
# Список — це ітерований об’єкт, і ми можемо отримати з нього ітератор за допомогою функції iter() в Python. 
# Ми отримали помилку з останнього стейтменту у цій програмі, тому що намагалися отримати наступний елемент,
# коли наступний елемент був недоступний (ітератор вичерпано). У таких випадках ми можемо вказати default-значення в якості другого параметра.

random = [5, 9, 'cat']
 
# Конвертуємо список в ітератор
random_iterator = iter(random)
print(random_iterator)
 
print(next(random_iterator))
 
print(next(random_iterator))
 
print(next(random_iterator))
 
# Це спричинить помилку.
# Ітератора вичерпано
print(next(random_iterator))

# Приклад №2: Передача default-значення у функцію next()

random = [5, 9]
 
# Конвертуємо список в ітератор
random_iterator = iter(random)
 
print(next(random_iterator, '-1'))
 
print(next(random_iterator, '-1'))
 
# random_iterator вичерпано
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))

