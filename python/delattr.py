# Функція delattr() видаляє вказаний атрибут із вказаного об’єкту.
# delattr(object, name)
# Функція delattr() приймає два параметри:
#    object — об’єкт, з якого потрібно видалити атрибут name;
#    name — рядок, який повинен бути іменем атрибута, що видаляється з object.

class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

delattr(Coordinate, 'z')

print('--After deleting z attribute--')
print('x = ', point1.x)
print('y = ', point1.y)

# Викличе помилку
print('z = ', point1.z)


# Видалення атрибута з використанням оператора del

class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

# Видаляємо атрибут z
del Coordinate.z

print('--After deleting z attribute--')
print('x = ', point1.x)
print('y = ', point1.y)

# Викличе помилку
print('z = ', point1.z)
