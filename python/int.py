# Функція int() конвертує число або рядок в еквівалентне ціле число.
# int(value, base)
# Функція int() приймає два параметри:
#    value — будь-який числовий рядок, байтовий об’єкт чи число;
#    base (не обов’язково) — система числення, в якій в поточний момент перебуває значення.


# Конвертуємо число з плаваючою крапкою в еквівалентне ціле число

result = int(9.9)
print('int(9.9):', result)


# Функція int() в Python з одним аргументом

# Функція int() із цілим числом
print("int(123) is:", int(123))

# Функція int() з числом з плаваючою крапкою
print("int(123.23) is:", int(123.23))

# Функція int() з числовим рядком
print("int('123') is:", int("123"))


# Функція int() із двома аргументами

# Конвертуємо рядок (у двійковому форматі) у ціле число
print("For 0b101, int is:", int("0b101", 2))

# Конвертуємо рядок (у вісімковому форматі) у ціле число
print("For 0o16, int is:", int("0o16", 8))

# Конвертуємо рядок (у шістнадцятковому форматі) у ціле число
print("For 0xA, int is:", int("0xA", 16))


# Функція int() з користувацькими об’єктами. Навіть якщо об’єкт не є числом,
# ми все одно можемо конвертувати його в цілий об’єкт, перевизначивши методи __index__() та __int__() класу,
# щоб вони повертали число. Ці два методи ідентичні. Нова версія Python використовує метод __index__().

class Person:
    age = 23

    def __index__(self):
        return self.age

    # def __int__(self):
    #     return self.age


person = Person()

# Функція int() з нецілочисельним об'єктом person
print("int(person) is:", int(person))
