# Функція ord() повертає цілочисельне представлення Unicode-символу.
# Ця функція є зворотною chr() для 8-бітних рядків і unichr() для об'єктів Unicode.
# Якщо довжина рядка більше одиниці, буде видана помилка TypeError.

character = 'P'

# Визначаємо цілочисельне представлення символу P
unicode_char = ord(character)
print(unicode_char)

print(ord('5'))
print(ord('A'))
print(ord('$'))


# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))
