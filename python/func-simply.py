# Приклад простої функції на 2 параметри

def addtwo(a, b):
    added = a + b
    return added


x = addtwo(11, 45435)  # Вказуємо аргументи для функції
print(x)

# Приклад функції на будь-яку кількість параметрів


def multi_func(*args):
    print(args)
    print(type(args))
    return sum(args)


# Вказуємо будь-яку кількість аргументів для функції
multi_sum = multi_func(5, 12, 44, 11, 49)
print(multi_sum)
