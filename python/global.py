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

# Example 2

a = 1


def foo_1():
    a = 1 + 2
    print(a, end=' ')


def foo_2():
    global a
    a = 1 + 2
    print(a, end=' ')


foo_1()
print(a)
# 3 1

foo_2()
print(a)
# 3 3
