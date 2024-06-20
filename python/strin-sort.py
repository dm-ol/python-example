# Сортування. Загалом, Python пропонує два різні способи сортування списків.
# Перший реалізований як функція з іменем sorted().

# Demonstrating the sorted() function:
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
