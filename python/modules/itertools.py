# У нашому випадку знадобиться islice, який бере "зріз" з генератора.
# В аргументах вказуємо об'єкт генератора та довжину зрізу.

from itertools import islice


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


slice = list(islice(fib(), 6))
print(slice)

# Output: [1, 1, 2, 3, 5, 8]
