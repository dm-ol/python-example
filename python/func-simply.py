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

# Приклад функції зі строкою


def author_info(name, book):
    info = f"{name} wrote {book} and other books"
    return info


info = author_info("John Do", "Black book")
print(info)

# Приклад функції з keywords arguments (аргумент з ключовими словами)


def author_info(name, book):
    info = f"{name} wrote {book} and other books"
    return info


# задали аргументи з ключовими словами, порядок не важливий
info = author_info(book="White book", name="Lindsey Dir")
print(info)
