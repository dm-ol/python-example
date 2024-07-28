# Функція setattr() встановлює значення для атрибута об’єкта.
# setattr(object, name, value)
# Якщо потрібно отримати атрибут об’єкта, використовуйте функцію getattr().
# Функція setattr() приймає три параметри:
#    object — об’єкт, атрибут якого має бути встановлено;
#    name — ім’я атрибута;
#    value — значення, що присвоюється атрибуту.

class Student:
    marks = 88
    name = 'Sheeran'


person = Student()

# Встановлюємо 'Adam' для name
setattr(person, 'name', 'Adam')
print(person.name)

# Встановлюємо 78 для marks
setattr(person, 'marks', 78)
print(person.marks)


# Як працює функція setattr() в Python?

class Person:
    name = 'Adam'


p = Person()
print('Before modification:', p.name)

# Встановлюємо 'John' для name
setattr(p, 'name', 'John')

print('After modification:', p.name)


# Коли атрибут не знайдено у функції setattr(). Якщо атрибут не знайдено,
# функція setattr() створює новий атрибут і надає йому значення.
# Проте це можливо лише в тому випадку, якщо об’єкт реалізовує метод __dict__().
# Ми можемо перевірити всі атрибути об’єкта за допомогою функції dir().

class Person:
    name = 'Adam'


p = Person()

# Встановлюємо атрибуту name значення 'John'
setattr(p, 'name', 'John')
print('Name is:', p.name)

# Встановлюємо атрибут, який не представлений у класі Person
setattr(p, 'age', 23)
print('Age is:', p.age)
