# Функція isinstance() перевіряє, чи є об’єкт (перший аргумент) екземпляром/об’єктом
# або підкласом класу (другий аргумент). Синтаксис функції isinstance(): isinstance(object, classinfo)

numbers = [1, 2, 3, 4, 2, 5]

# Перевіряємо, чи є numbers об'єктом класу list
result = isinstance(numbers, list)
print(result)

# Приклад №1: Як працює функція isinstance()?


class Foo:
    a = 5


fooInstance = Foo()

print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))

# Приклад №2: Робота функції isinstance() із вбудованими типами

numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers, 'instance of list?', result)

result = isinstance(numbers, dict)
print(numbers, 'instance of dict?', result)

result = isinstance(numbers, (dict, list))
print(numbers, 'instance of dict or list?', result)

number = 5

result = isinstance(number, list)
print(number, 'instance of list?', result)

result = isinstance(number, int)
print(number, 'instance of int?', result)
