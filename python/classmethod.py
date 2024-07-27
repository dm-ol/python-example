# Функція classmethod() повертає метод класу для вказаної функції.
# У новіших версіях Python ви можете використовувати декоратор @classmethod для визначення методу класу. Наприклад:
#       @classmethod
#       def func(cls, args...)

# Створення методу класу за допомогою функції classmethod()
# Тут у нас є клас Person, який має змінну-член age, якій присвоєно значення 25. Ми також маємо метод printAge(), який приймає один параметр cls.
# Параметр cls приймає в якості аргументу клас Person, а не об’єкт класу Person. Потім ми передаємо метод Person.printAge як аргумент у функцію classmethod().
# Це конвертує даний метод у метод класу, щоб він приймав перший параметр як клас (тобто Person).
# В останньому рядку ми викликаємо printAge() без створення об’єкта Person, як це робиться зі статичними методами. Це виводить змінну age.

from datetime import date


class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)


# Створюємо метод класу printAge()
Person.printAge = classmethod(Person.printAge)

Person.printAge()


# Коли слід використовувати метод класу?
# 1. Фабричні методи
# Фабричні методи — це методи, які повертають об’єкт класу (наприклад, конструктор) для різних варіантів використання.
# Це схоже на перевантаження функцій у С++. Оскільки в Python нічого такого немає, то використовуються методи класу та статичні методи.

# Створення фабричного методу з використанням методу класу


# Випадковий Person. Тут об’єкт створюють:
#    Конструктор, який приймає звичайні параметри name та age.
#    Метод fromBirthYear(), який в якості першого параметра cls приймає клас Person (не об’єкт класу Person) і повертає конструктор, викликаючи cls(name, date.today().year - birthYear), що еквівалентно Person(name, date.today().year - birthYear).
# Перед методом fromBirthYear() ми бачимо @classmethod. Це декоратор для перетворення fromBirthYear() в метод класу.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()
