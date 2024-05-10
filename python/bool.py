# Функція bool() приймає вказаний аргумент та повертає його логічне значення.
# Функція bool() повертає:
#   False — якщо argument порожній, False, 0 або None.
#   True — якщо argument є будь-яким числом (крім 0), True або рядок.

test = 254
# bool() з цілим числом
print(test, 'is', bool(test))

test1 = 25.14
# bool() з числом з плаваючою крапкою
print(test1, 'is', bool(test1))

test2 = 'Python is the best'
# bool() з рядком
print(test2, 'is', bool(test2))

test3 = True
# bool() з True
print(test3, 'is', bool(test3))

test = []
# bool() з порожнім аргументом
print(test, 'is', bool(test))

test1 = 0
# bool() з нулем
print(test1, 'is', bool(test1))

test2 = None
# bool() з None
print(test2, 'is', bool(test2))

test3 = False
# bool() з False
print(test3, 'is', bool(test3))
