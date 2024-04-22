# Надання функції меншої кількості аргументів, ніж вона очікує, називається
# частковим застосуванням функцій (в прикладі — partial зі стандартної бібліотеки functools).
# Іншими словами, часткове застосування — це коли функція приймає іншу функцію
# з кількома параметрами та повертає функцію, але вже з меншою кількістю параметрів.


from functools import partial


def greet(greeting, separator, emphasis, name):
    print(f'{greeting}{separator} {name}{emphasis}')


newfunc = partial(greet, greeting='Hello', separator=',', emphasis='.')

newfunc(name='Sviatoslav')  # Output: Hello, Sviatoslav.
newfunc(name='Adrian')  # Output: Hello, Adrian.
