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

# Створюємо клас


class Bike:
    name = ""
    gear = 0


# Створюємо об'єкт класу
bike1 = Bike()

# Отримуємо доступ до атрибутів об'єкта та присвоюємо нові значення
bike1.gear = 11
bike1.name = "Mountain Bike"

# Виводимо дані об'єкта на екран
print(f"Name: {bike1.name}, Gears: {bike1.gear} ")


# Створення кількох об’єктів одного класу
# Ми можемо створити багато об’єктів одного класу. Наприклад:

# Створюємо клас
class Employee:
    # Визначаємо атрибут
    employee_id = 0


# Створюємо два об'єкти класу Employee
employee1 = Employee()
employee2 = Employee()

# Отримуємо доступ до атрибутів об'єкта employee1 та присвоюємо нове значення
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# Отримуємо доступ до атрибутів об'єкта employee2 та присвоюємо нове значення
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")
