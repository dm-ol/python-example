# Функція property() використовується для визначення властивостей в класах.
# Синтаксис функції property(): property(fget=None, fset=None, fdel=None, doc=None)

# Функція property() приймає 4 необов’язкові параметри:
#    fget (не обов’язково) — функція для отримання значення атрибута. За замовчуванням використовується None;
#    fset (не обов’язково) — функція для встановлення значення атрибута. За замовчуванням використовується None;
#    fdel (не обов’язково) — функція для видалення значення атрибута. За замовчуванням використовується None;
#    doc (не обов’язково) — рядок, який містить документацію (рядок документації) для атрибута. За замовчуванням використовується None.

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
