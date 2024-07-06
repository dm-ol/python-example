# Доступ до елементів кортежу з використанням індексації
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

print(letters[0])   # виведе "p"
print(letters[5])   # виведе "a"

# Доступ до елементів кортежу з використанням від'ємної індексації
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(letters[-1])   # виведе 'z'
print(letters[-3])   # виведе 'm'

# Доступ до елементів кортежу за допомогою зрізу
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# Виводимо "зрізані" елементи з 2 по 4 індекс
print(my_tuple[2:4])

# Виводимо елементи до 2-го індексу – від'ємна індексація
print(my_tuple[:-7])

# Виводимо елементи з 7-го індексу до останнього
print(my_tuple[7:])

# Виводимо всі елементи кортежу
print(my_tuple[:])

# У Python методи, які додають або видаляють елементи, не працюють з кортежами. Працюють лише наступні два методи count, index:

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # рахує кількість 'р', виведе 2

print(my_tuple.index('l'))  # показує номер в кортежі, виведе 3

# Ми можемо використовувати цикл for для перебору елементів кортежу. Наприклад:

languages = ('Python', 'Swift', 'C++')

# Перебираємо та виводимо елементи кортежу
for language in languages:
    print(language)

# Об'єднуємо кортежі

all_t = languages + my_tuple

print(all_t)

# Зміна кортежу, шляхом конвертації у список і назад:

t_set = (255, 322, 190)

print(t_set)

l_set = list(t_set)
l_set.append(662)

t_set2 = tuple(l_set)
print(t_set2)
