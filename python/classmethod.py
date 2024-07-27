# Функція classmethod() повертає метод класу для вказаної функції.
# У новіших версіях Python ви можете використовувати декоратор @classmethod для визначення методу класу. Наприклад:
#       @classmethod
#       def func(cls, args...)

# Створення методу класу за допомогою функції classmethod()

class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)


# Створюємо метод класу printAge()
Person.printAge = classmethod(Person.printAge)

Person.printAge()
