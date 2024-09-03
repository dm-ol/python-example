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


# Приклад використання конструктора за замовчуванням разом із параметризованим конструктором в Python:

class MyClass:
    def __init__(self, name=None):
        if name is None:
            print("Default constructor called")
        else:
            self.name = name
            print("Parameterized constructor called with name", self.name)

    def method(self):
        if hasattr(self, 'name'):
            print("Method called with name", self.name)
        else:
            print("Method called without a name")


# Створюємо об'єкт класу за допомогою конструктора за замовчуванням
obj1 = MyClass()

# Викликаємо метод класу через об'єкт obj1
obj1.method()

# Створюємо об'єкт класу за допомогою параметризованого конструктора
obj2 = MyClass("John")

# Викликаємо метод класу через об'єкт obj2
obj2.method()
# Результат:

# Default constructor called
# Method called without a name
# Parameterized constructor called with name John
# Method called with name John

# Тут ми визначаємо клас MyClass з конструктором за замовчуванням та параметризованим конструктором.

#    Конструктор за замовчуванням перевіряє, чи передано параметр,
#    і виводить відповідне повідомлення на екран. Якщо параметр не вказано,
#    викликається конструктор за замовчуванням, якщо вказано, то викликається параметризований конструктор.

#    Параметризований конструктор приймає параметр, який присвоює атрибуту (члену класу) name.

#    Ми також визначаємо метод method(), який перевіряє наявність або відсутність в об’єкта атрибута name
#    і виводить відповідне повідомлення на екран.

# Ми створюємо два об’єкти класу MyClass, використовуючи обидва типи конструкторів.

#    Спочатку ми створюємо об’єкт за допомогою конструктора за замовчуванням — виводиться Default constructor called.
#    Потім ми викликаємо у цього об’єкта метод method(), який виводить на екран повідомлення Method called without a name.

#    Потім ми створюємо об’єкт за допомогою параметризованого конструктора, передавши йому ім’я "John".
#    Конструктор викликається автоматично і на екран виводиться повідомлення Parameterized constructor
#    called with name John. Потім ми викликаємо у цього об’єкта метод method(), який виводить на екран
#    повідомлення Method called with name John.

# Загалом цей приклад показує, як в одному класі можна використовувати відразу обидва типи конструкторів.

# Переваги використання конструкторів в Python
#    Ініціалізація об’єктів. Конструктори використовуються для ініціалізації об’єктів класу.
#    Вони дозволяють встановити значення за замовчуванням для членів класу,
#    а також ініціалізувати об’єкт користувацькими даними.

#    Простота реалізації. Конструктори легко реалізувати в Python за допомогою методу __init__().

#    Покращення читабельності коду. Конструктори покращують читабельність коду, оскільки дають зрозуміти,
#    які значення ініціалізуються і як вони ініціалізуються.

#    Інкапсуляція. Конструктори можуть використовуватися для забезпечення інкапсуляції, гарантуючи,
#    що члени об’єкта ініціалізуються коректно та контрольовано.

# Недоліки використання конструкторів в Python
#    Обмежена функціональність. Конструктори в Python мають обмежену функціональність порівняно
#    з конструкторами з інших мов програмування. Наприклад, у Python немає конструкторів з модифікаторами доступу,
#    такими як public, private або protected.

#    Конструктори можуть бути непотрібними. У деяких випадках конструктори можуть бути непотрібними,
#    оскільки є достатньо значень за замовчуванням для членів класу. У таких випадках використання
#    конструктора може призвести до зайвого ускладнення коду.

# В цілому, конструктори в Python можуть бути корисними для ініціалізації об’єктів та забезпечення інкапсуляції.
# Однак вони не завжди є необхідними та мають обмежену функціональність у порівнянні з конструкторами в інших мовах програмування.
