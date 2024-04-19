# Різні перевірки коду

# Example 1
a = 15


def func_1():
    x = 33
    b = 48
    a = x + b
    print(a)
    return a


func_1()


print(a)
# print(b)  # Not define

# Example 2 (Global)

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
