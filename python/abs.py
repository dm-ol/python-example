# Функція abs() повертає абсолютне значення вказаного числа.
# Якщо число є комплексним, функція abs() повертає його величину.

number = -20

absolute_number = abs(number)
print(absolute_number)

# Приклад №1: Отримання абсолютного значення числа

# Випадкове ціле число
integer = -20
print('Absolute value of -20 is:', abs(integer))

# Випадкове число з плаваючою крапкою
floating = -30.33
print('Absolute value of -30.33 is:', abs(floating))


# Приклад №2: Отримання величини комплексного числа

# Випадкове комплексне число
complex = (3 - 4j)
print('Magnitude of 3 - 4j is:', abs(complex))
