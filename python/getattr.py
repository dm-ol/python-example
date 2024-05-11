# Функція getattr() повертає значення іменованого атрибута об’єкта.
# Якщо його не знайдено, то повертається значення за замовчуванням, надане функцією.
# Синтаксис функції: getattr(object, name[, default])

# Функція getattr() приймає декілька параметрів:
#   object — значення іменованого атрибута, яке має бути повернуто;
#   name — рядок, який містить ім’я атрибута;
#   default (не обов’язково) — значення, яке повертається, коли іменований атрибут не знайдено.

class Student:
    marks = 88
    name = 'Sheeran'


person = Student()

name = getattr(person, 'name')
print(name)

marks = getattr(person, 'marks')
print(marks)
