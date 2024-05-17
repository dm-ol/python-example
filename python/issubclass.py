# Функція issubclass() в Python використовується для перевірки того, чи є клас підкласом іншого класу, чи ні.
# Синтаксис функції issubclass(): issubclass(class, classinfo)

# Example

class Person:
    name = "John"
    age = 23


class Employee (Person):
    salary = 4200.00


print(issubclass(Employee, Person))

# Examle_2


class Polygon:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)


class Triangle(Polygon):
    def __init__(self):

        Polygon.__init__('triangle')


print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))
