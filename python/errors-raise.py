# Ключове слово raise використовується для створення винятку. Ви можете визначити,
# який тип помилки викликати, і текст, який потрібно надрукувати користувачеві.

# Example 1


def nums_div(a, b):  # Генерація помилки ValueError
    if b == 0:
        raise ValueError("Second argument can't be 0")
    return a / b


try:
    nums_div(12, 0)
except Exception as err:
    print(err)

# Example 2
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
