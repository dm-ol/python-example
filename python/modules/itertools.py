# У нашому випадку знадобиться islice, який бере "зріз" з генератора.
# В аргументах вказуємо об'єкт генератора та довжину зрізу.

from itertools import cycle, islice
from itertools import islice


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


slice = list(islice(fib(), 6))
print(slice)

# Output: [1, 1, 2, 3, 5, 8]

# Функція cycle() з itertools приймає на вхід об'єкт, що ітерується,
# і створює нескінченний ітератор, що циклічно повертає елементи даного об'єкта.
# Фішка в тому, що коли елементи послідовності закінчуються, ітерація починається знову з першого елемента.
# Але якщо ви проходите циклом по такому ітератору, то важливо передбачити вихід з циклу,
# інакше він стане нескінченним (як у нас в першому випадку на картинці).
# Ми також можемо скористатися islice(), який поверне ітератор по підмножині переданого об'єкта.


colors = cycle(['red', 'white', 'blue'])

for item in colors:
    print(item, end=' ')

# Output: red white blue red white blue...

for color in islice(colors, 3, 5):
    print(color, end=' ')

# Output: red white
