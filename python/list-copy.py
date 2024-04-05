# Скопіювати список можна декількома способами.
# Копіювання за допомогою [:]:
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
print(my_list)

your_list = my_list[:]
print(your_list)

# Копіювання за допомогою copy:

my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
print(my_list)

your_list = my_list.copy()
print(your_list)

# Копіювання за допомогою list:

my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
print(my_list)

your_list = list(my_list)
print(your_list)
