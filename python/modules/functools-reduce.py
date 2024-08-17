# Модуль functools дозволяє розкрити функціональні можливості Python — наприклад,
# функція reduce дозволяє стискати дані, застосовуючи послідовно функцію і запам'ятовуючи результат.
# Таким чином, у прикладі reduce множить 1 на 2, потім результат множить на 3 і так далі.

from functools import reduce


def multiply(a, b):
    return a * b


result = reduce(multiply, [1, 2, 3, 4, 5])
print(result)

# Output: 120
