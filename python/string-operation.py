# Операції над рядками

str1 = 'abc'
str2 = 'xyz'

# оператор +, що використовується для двох або більше рядків,
# створює новий рядок, що містить усі символи з його аргументів (примітка: порядок має значення)
print(str1 + str2)
print(str2 + str1)

# оператору * потрібні рядок і число як аргументи; у цьому випадку порядок не має значення – ви можете поставити число перед рядком,
# або навпаки, результат буде той самий – новий рядок, створений n-ою копією рядка аргументу.
print(5 * 'a')
print('b' * 4)

# Примітка: скорочені варіанти наведених вище операторів також застосовуються до рядків (+=і*=).


# Оператор in (він просто перевіряє, чи його лівий аргумент (рядок) можна знайти будь-де в межах правого аргументу (іншого рядка)).

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

# Оператор not in (він просто перевіряє, чи його лівий аргумент (рядок) відсутній в межах правого аргументу (іншого рядка)).

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

# Функція min() для рядків (відповідає номеру таблиці ASCII)

# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))


# Функція max() для рядків (відповідає номеру таблиці ASCII)

# Demonstrating min() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))
