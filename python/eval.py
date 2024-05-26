# Функція eval() оцінює вказаний вираз. Якщо вираз є допустимим Python-стейтментом,
# то його буде виконано. Синтаксис функції eval(): eval(вираз, globals=None, locals=None)
# Функція eval() приймає три параметри:
#   вираз — рядок, який аналізується та оцінюється як Python-вираз;
#   globals (не обов’язково) — словник;
#   locals (не обов’язково) — об’єкт для зіставлення. Словник — це стандартний тип зіставлення, який часто використовується в Python.

number = 9

# Функція eval() виконує операцію множення
square_number = eval('number * number')
print(square_number)

# Приклад №2: Практичний приклад для демонстрації використання функції eval()

# Периметр квадрата


def calculatePerimeter(l):
    return 4*l

# Площа квадрата


def calculateArea(l):
    return l*l


expression = input("Type a function: ")

for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print("If length is ", l, ", Perimeter = ", eval(expression))
    elif (expression == 'calculateArea(l)'):
        print("If length is ", l, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break
