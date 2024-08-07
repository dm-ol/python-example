# Функція iter() повертає ітератор для вказаного аргументу.
# Синтаксис функції iter(): iter(object, sentinel)

# Список телефонів
phones = ['apple', 'samsung', 'oneplus']
phones_iter = iter(phones)

print(next(phones_iter))
print(next(phones_iter))
print(next(phones_iter))

# Приклад №1: Функція iter() в Python

# Список голосних
vowels = ["a", "e", "i", "o", "u"]

# Функція iter() зі списком голосних
vowels_iter = iter(vowels)

print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))

# Приклад №2: Функція iter() з об’єктами користувача


class PrintNumber:
    def __init__(self, max):
        self.max = max

# Функція iter() у класі
    def __iter__(self):
        self.num = 0
        return self
# Функція next() у класі

    def __next__(self):
        if (self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num


print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print(next(print_num_iter))
print(next(print_num_iter))
print(next(print_num_iter))


# Приклад №3: Функція iter() із параметром sentinel

class DoubleIt:

    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__


my_iter = iter(DoubleIt(), 16)

for x in my_iter:
    print(x)
