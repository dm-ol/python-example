# Функція hasattr() повертає True, якщо об’єкт має вказаний іменований атрибут, та False, якщо його немає.
# Синтаксис функції hasattr(): hasattr(object, name)

# Функція hasattr() приймає два параметри:
#    object — об’єкт, іменований атрибут якого необхідно перевірити;
#    name — ім’я атрибута, за яким здійснюється пошук.

class Person:
    age = 23
    name = "Adam"


person = Person()

print("Person's age:", hasattr(person, "age"))
print("Person's salary:", hasattr(person, "salary"))

# Функція hasattr() в Python


class Car:
    brand = "Ford"
    number = 7786


car = Car()

print("The car class has brand:", hasattr(Car, "brand"))
print("The car class has number:", hasattr(Car, "number"))
print("The car class has specs: ", hasattr(Car, "specs"))
