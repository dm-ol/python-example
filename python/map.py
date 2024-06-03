# Функція map() виконує вказану функцію до кожного елементу ітерованого об’єкта (списку, кортежу тощо)
# та повертає ітератор, який містить результати.
# Синтаксис функції map(): map(func, *iterables)
# Функція map() приймає два параметри:
#   func — функція, яка застосовується до кожного елемента ітерованого об’єкта;
#   *iterables — будь-яка кількість ітерованих об’єктів (таких як множини, списки, кортежі тощо), може бути більше одного.

numbers = [2, 4, 6, 8, 10]

# Повертає число в квадраті


def square(number):
    return number * number


# Застосовуємо функцію square() до кожного елементу списку
squared_numbers_iterator = map(square, numbers)

# Конвертуємо в список
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)


# Приклад №1: Робота функції map()

def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# Конвертуємо об'єкт map у множину
numbersSquare = set(result)
print(numbersSquare)


# Приклад №2: Як використовувати лямбда-функцію з функцією map()?

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# Конвертуємо об'єкт map у множину
numbersSquare = set(result)
print(numbersSquare)


# Приклад №3: Передача кількох ітераторів у функцію map() з використанням лямбда-функції

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))
