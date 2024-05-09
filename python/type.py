# Функція type() повертає тип об’єкта в Python

prime_numbers = [2, 3, 5, 7]

# Перевіряємо тип об'єкта prime_numbers
result = type(prime_numbers)
print(result)


# Функція type() має дві різні форми:


# Функція type() з одним параметром. Функція type() повертає:
#   тип об’єкта, якщо вказано лише один параметр object;
#   новий тип, якщо вказано три параметри.

numbers_list = [1, 2]
print(type(numbers_list))

numbers_dict = {1: 'one', 2: 'two'}
print(type(numbers_dict))


class Foo:
    a = 0


foo = Foo()
print(type(foo))

# Функція type() з трьома параметрами  type(name, bases, dict)

o1 = type('X', (object,), dict(a='Foo', b=12))
print(type(o1))

print(vars(o1))


class test:
    a = 'Foo'
    b = 12


o2 = type('Y', (test,), dict(a='Foo', b=12))
print(type(o2))
print(vars(o2))
