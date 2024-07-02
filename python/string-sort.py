# Сортування. Загалом, Python пропонує два різні способи сортування списків.
# Перший реалізований як функція з іменем sorted().

# Demonstrating the sorted() function:
from math import pi
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Другий спосіб впливає на сам список – новий список не створюється.
# Упорядкування виконується на місці методом, названим sort().

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)


# f-рядки — зручний спосіб включення значення виразу всередині рядків (з версії 3.6).

# 🔴str.format() — повертає копію рядка, в якому на місці {} буде поставлено зазначені аргументи.

# 🔴оператор % — форматування по-старому: в стилі C.


s = f'pi: {pi: .3f}'    # pi: 3.142
print(s)

num = 714
s = f'ThePyU: {num}'    # 'ThePyU: 714'
print(s)

d = {'one': 1}
s = f"one: {d['one']}"    # 'one: 1'
print(s)

s = '''The {} Universe:
{value}'.format('Python', value=714)
# 'The Python Universe: 714'''
print(s)

num = 4
s = 'string: %s' % num    # 'string: 4'
print(s)
