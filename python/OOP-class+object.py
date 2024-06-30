# Визначення класу в Python
# Для створення класу в Python використовується ключове слово class:
# Тут ми створили клас з ім’ям ClassName.

class ClassName:
    # Визначення класу


class Bike:
    name = ""
    gear = 0
# Тут:
    #    Bike – назва класу;
    #    name та gear — змінні всередині класу.

# Об’єкт — це екземпляр класу. Наприклад, Bike — це клас і ми можемо створити об’єкти типу bike1, bike2 з цього класу.

# Синтаксис створення об’єктів класу в Python:


objectName = ClassName()

# Розглянемо приклад:

# Створюємо клас


class Bike:
    name = ""
    gear = 0


# Створюємо об'єкт класу
bike1 = Bike()
# Тут bike1 — це об’єкт класу Bike. Ми можемо використовувати цей об’єкт для доступу до атрибутів (даних) класу Bike.

# Доступ до атрибутів класу через об’єкти
# Оператор . використовується для доступу до атрибутів класу. Наприклад:

# Змінюємо атрибут name об'єкта bike1
bike1.name = "Mountain Bike"

# Отримуємо доступ до атрибута gear об'єкта bike1
bike1.gear
# Тут ми використали bike1.name та bike1.gear для доступу та зміни значень атрибутів name та gear.
