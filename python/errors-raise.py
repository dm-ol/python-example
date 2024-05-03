# Ключове слово raise використовується для створення винятку. Ви можете визначити,
# який тип помилки викликати, і текст, який потрібно надрукувати користувачеві.

# Example 1
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# Example 2


def nums_div(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0")
    return a / b
