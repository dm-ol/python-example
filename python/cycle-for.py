# Цикл for використовується для виконання блоку коду певну кількість разів. Він використовується
# з будь-якими послідовностями, такими як списки, кортежі, рядки та ін., які можна перебирати (наприклад, рядків).
# Використовуються для dict, list, tuple, str, set, range.
# За допомогою циклу for можна перебирати послідовність чисел, використовуючи вбудовану функцію range.

languages = ['Swift', 'Python', 'Go', 'JavaScript']

# Отримуємо доступ до елементів списку, використовуючи цикл for
for language in languages:
    print(language)

# example 2
word = "Python"
for letter in word:
    print(letter, end="*")

# Діапазон — це ряд значень між двома числовими інтервалами. У Python використовується вбудована функція range() для визначення діапазону значень. Наприклад:
# Використовуємо функцію range() для визначення діапазону значень
values = range(4)

# Виконуємо ітерації з i = 0 до i = 3
for i in values:
    print(i)

# приклад 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# Простий приклад циклу for
names = ["Денис", "Василь", "Валерій", "Олександра", "Сергій", "Яна"]
for name in names:
    print("Поздоровляю,", name, "!")

# Списки можна перебирати за допомогою циклу for, наприклад:
my_list = ["білий", "пурпурний", "блакитний", "жовтий", "зелений"]

for color in my_list:
    print(color)

# Цикл for також може мати необов’язковий блок else, який виконується після завершення циклу.

digits = [0, 1, 4]

for i in digits:
    print(i)
else:
    print("No items left.")


# Цикл for зі словником (dict)

cars_price = {"Audi Q8": 86000,
              "BMW X6": 80000,
              "Mercedes GLE": 92000
              }

for car in cars_price:
    # де car - ключ,  car_price[car] - значення ключа
    print(car, cars_price[car])

# Цикл for зі словником (dict) з методом items

cars_price = {"Audi Q8": 86000,
              "BMW X6": 80000,
              "Mercedes GLE": 92000
              }

for car in cars_price.items():
    # де car - ключ,  price - значення ключа
    car, price = car
    print(car, price)
