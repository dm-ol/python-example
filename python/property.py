# Функція property() використовується для визначення властивостей в класах.

# Python-програма для пояснення роботи функції property()

# Клас Alphabet
class Alphabet:
    def __init__(self, value):
        self._value = value

    # Отримання значень
    def getValue(self):
        print('Getting value')
        return self._value

    # Встановлення значень
    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

    # Видалення значень
    def delValue(self):
        print('Deleting value')
        del self._value

    value = property(getValue, setValue, delValue)


# Передаємо значення
x = Alphabet('Acode')
print(x.value)

x.value = 'Acd'

del x.value
