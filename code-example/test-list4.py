# Створіть новий список з 5-ма елементами
my_list = [4, 2, 'a', 23, 15]
print("Початковий список:", my_list)

# Видаліть 3-й елемент
my_list.pop(2)
print("Видалили 3-й елемент:", my_list)

# Виведіть в термінал довжину списку
print("Довжина списка:", len(my_list))

# Змініть порядок послідовності елементів в списку
my_list.reverse()
print("Реверс списку:", my_list)

# Створіть ще один список з 2-ма елементами
your_list = [5, 32]
print("Новий список:", your_list)

# Доповніть перший список елементами з другого списку
my_list.extend(your_list)

# Виведіть в термінал остаточний спирсок з 6-ти елементів
print("Остаточний список:", my_list)

# Створити ще один додатковий список
our_list = ['rc', 17, {'key': 888}, 94]
print("Додатковий список:", our_list)

# Поєднати списки

combolist = my_list + our_list
print("Об'єднаний список:", combolist)
