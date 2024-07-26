# Функція str() повертає рядкове представлення вказаного об’єкта.
# str(object, encoding='utf-8', errors='strict'), параметри encoding та errors призначені лише для використання, коли тип object — це байти або байтовий масив.
# Функція str() приймає три параметри:
#    object — об’єкт, рядкове представлення якого потрібно повернути;
#    encoding (не обов’язково) — кодування, в яке потрібно декодувати даний байтовий об’єкт (може використовуватися UTF-8, ASCII тощо). За замовчуванням використовується utf-8;
#    errors (не обов’язково) — відповідь при невдалому декодуванні (може бути strict, ignore, replace тощо).

# Рядкове представлення Adam
print(str('Adam'))


# Функція str() в Python

# Рядкове представлення Luke
name = str('Luke')
print(name)

# Рядкове представлення цілого числа 40
age = str(40)
print(age)

# Рядкове представлення числового рядка 7ft
height = str('7ft')
print(height)


# Функція str() з байтовими об’єктами

# Оголошуємо байтовий об'єкт
b = bytes('pythön', encoding='utf-8')

# Конвертуємо байтовий об'єкт utf-8 в ascii з помилкою ignore
print(str(b, encoding='ascii', errors='ignore'))

# Конвертуємо байтовий об'єкт utf-8 в ascii з помилкою strict
print(str(b, encoding='ascii', errors='strict'))

# У першому прикладі ми створили байтовий об’єкт b з рядком pythön та кодуванням utf-8.
# Ми передали об’єкт b у функцію str() і вказали кодування ascii.
# Параметру errors ми встановили значення ignore, тому функція str() ігнорує символ ö.
# Оскільки функція не може декодувати цей символ у ascii, ми отримуємо у виводі pythn.
# Аналогічно, у другому прикладі ми встановили помилку strict.
# У цьому випадку функція str() бере до уваги символ ö і генерує виняток UnicodeDecodeError у виводі.