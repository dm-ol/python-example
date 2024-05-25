# Функція dir() повертає список допустимих атрибутів переданого об’єкту.
import math
print("dir для строки")
number = 'bark'
print(dir(number))

print("dir для integer")
number = int(12)
print(dir(number))

print("dir для float")
number = float(12)
print(dir(number))

print("dir для списку")
list_1 = [11, 12, 13, 14]
print(dir(list_1))

print("dir для кортежу")
tuple_list = (1, 12, 42, 55)
print(dir(tuple_list))

print("dir для словника")
dict_1 = {
    'Brand': 'Honda',
    'Model': 'CR-V',
    'Type': 'Hybrid',
}
print(dir(dict_1))

# Наприклад, ви можете запустити такий код, щоб надрукувати імена всіх атрибутів (на літеру t) у математичному модулі:

print("dir для MATH")
for name in dir(math):
    print(name, end="∖t")
