# Функція bin() конвертує вказане ціле число у його двійкове представлення та повертає його.

number = 15

# Конвертуємо 15 у двійковий формат
print('The binary equivalent of 15 is', bin(number))

# Приклад №1: Функція bin() в Python

number = 5

# Конвертуємо 5 у двійковий еквівалент
print('The binary equivalent of 5 is:', bin(number))


# Приклад №2: Функція bin() з “нецілочисельним” класом в Python

class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def func():
        return apple + orange + grapes


print('The binary equivalent of quantity is:', bin(Quantity()))

# Приклад №3: Функція bin() з методом __index__() для “нецілочисельного класу”


class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def __index__(self):
        return self.apple + self.orange + self.grapes


print('The binary equivalent of quantity is:', bin(Quantity()))
