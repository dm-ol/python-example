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
