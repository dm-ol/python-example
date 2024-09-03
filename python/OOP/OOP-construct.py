# Конструктори зазвичай використовуються для ініціалізації об’єктів класу.
# Їх завдання полягає у присвоюванні значень членам класу.
# В Python метод __init__() називається конструктором і завжди викликається при створенні об’єкта.

# Синтаксис оголошення конструктора в Python:
# def __init__(self):
#     Тіло конструктора

# Типи конструкторів:
#    Конструктор за замовчуванням — це простий конструктор, який не приймає жодних параметрів. Його визначення має тільки один параметр, яким є посилання на створюваний об’єкт.
#    Параметризований конструктор — це конструктор з параметрами: перший параметр — це посилання на створюваний об’єкт (self), а інші параметри надаються програмістом.

# Приклад конструктора за замовчуванням в Python:
class GeekforGeeks:

    # Конструктор за замовчуванням
    def __init__(self):
        self.geek = "Ravesli"

    # Виводимо дані
    def print_Geek(self):
        print(self.geek)


# Створюємо об'єкт класу
obj = GeekforGeeks()

# Викликаємо метод класу через об'єкт obj
obj.print_Geek()
# Результат:
# Ravesli


# Приклад параметризованого конструктора в Python:

class Addition:
    first = 0
    second = 0
    answer = 0

    # Параметризований конструктор
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# Створюємо об'єкт класу.
# При цьому викликається параметризований конструктор
obj1 = Addition(1000, 2000)

# Створюємо другий об'єкт того ж класу
obj2 = Addition(10, 20)

# Виконуємо операцію додавання через об'єкт obj1
obj1.calculate()

# Виконуємо операцію додавання через об'єкт obj2
obj2.calculate()

# Виводимо на екран результат роботи об'єкта obj1
obj1.display()

# Виводимо на екран результат роботи об'єкта obj2
obj2.display()
# Результат:

# First number = 1000
# Second number = 2000
# Addition of two numbers = 3000
# First number = 10
# Second number = 20
# Addition of two numbers = 30
