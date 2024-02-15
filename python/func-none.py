# якщо функція не повертає певне значення за допомогою інструкції return,
# то вважається, що вона неявно повертає None.
def strange_function(n):
    if (n % 2 == 0):
        return True


print(strange_function(2))
print(strange_function(1))
