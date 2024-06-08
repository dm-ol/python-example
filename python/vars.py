# Функція vars() повертає атрибут __dict__ (відображення словника) вказаного об’єкта.

# Приклад №1: Функція vars() в Python

# Функція vars() без вказування аргументу
print(vars())

# Повертаємо __dict__ об'єкта dict
print(vars(dict))

# Приклад №2: Функція vars() з аргументом без атрибута __dict__

string = "Jones"

# Функція vars() з рядком (error)
print(vars(string))

# Приклад №3: Функція vars() з користувацьким об’єктом


class Fruit:
    def __init__(self, apple=5, banana=10):
        self.apple = apple
        self.banana = banana


eat = Fruit()

# Повертаємо __dict__ об'єкта eat
print(vars(eat))
