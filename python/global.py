# Якщо потрібно вказати глобальну змінну у тілі функції, можна використати global

a = 15


def func_1():
    x = 33
    global b
    b = 48
    a = x + b
    print(a)
    return a


func_1()


print(a)
print(b)
