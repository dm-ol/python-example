# В Python лямбда-функція (або “анонімна функція”) — це спеціальний тип функції без імені.
# Ключове слово lambda (замість def) використовується для створення лямбда-функції. lambda аргумент(и) : вираз

# Оголошуємо лямбда-функцію
# greet = lambda : print('Hello, World!')
def greet(): return print('Hello, World!')


# Викликаємо лямбда-функцію
greet()


# Лямбда-функція, яка приймає 1 аргумент
# greet_user = lambda name : print('Hey there,', name)
def greet_user(name): return print('Hey there,', name)


# Виклик лямбда-функції
greet_user('Delilah')


# Функція filter() в Python приймає функцію та ітерований об’єкт (списки, кортежі та рядки) як аргументи.
# Функція викликається зі всіма елементами в списку, і повертається новий список, що містить елементи,
# для яких функція визначила значення True. Наприклад:

# Програма фільтрації лише парних елементів зі списку
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)


# Функція map() в Python приймає функцію та об’єкт, що ітерується (списки, кортежі та рядки) як аргументи.
# Функція викликається зі всіма елементами у списку і повертається новий список, який містить елементи,
# що повертаються цією функцією для кожного елемента.

# Програма подвоєння значень кожного елемента списку за допомогою функції map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)
