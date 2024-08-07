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


# Створення атрибута з функціями геттера, сеттера та делітера

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Встановлюємо властивість для використання методів get_name, set_name та del_name
    name = property(get_name, set_name, del_name, 'Name property')


p = Person('Adam')
print("The name is:", p.name)
p.name = 'John'
del p.name


# Використання декоратора @property

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name


p = Person('Adam')
print('The name is:', p.name)
p.name = 'John'
del p.name

# Тут замість використання функції property() ми використали декоратор @property.

# По-перше, ми вказуємо, що метод name() є атрибутом класу Person. Це робиться за допомогою @property перед геттером,
# як показано у програмі. Далі ми використовуємо атрибут name для вказівки сеттера та делітера.
# Це робиться за допомогою @name.setter для методу сеттера та @name.deleter для методу делітера.
# Зверніть увагу на те, що ми використали той же метод name() з різними визначеннями для визначення геттера, сеттера та делітера.

# Тепер, коли ми використовуємо p.name, він внутрішньо (під капотом) викликає відповідний геттер, сеттер і делітер.
