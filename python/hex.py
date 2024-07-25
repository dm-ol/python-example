# Функція hex() в Python використовується для перетворення десяткового числа у відповідне йому шістнадцяткове представлення.

decimal_number = 999
hexadecimal_value = hex(decimal_number)

print(hexadecimal_value)


# Як працює функція hex()?

number = 435
print(number, 'in hex =', hex(number))

number = 0
print(number, 'in hex =', hex(number))

number = -34
print(number, 'in hex =', hex(number))

returnType = type(hex(number))
print('Return type from hex() is', returnType)


# Шістнадцяткове представлення числа з плаваючою крапкою

number = 2.5
print(number, 'in hex =', float.hex(number))

number = 0.0
print(number, 'in hex =', float.hex(number))

number = 10.5
print(number, 'in hex =', float.hex(number))
