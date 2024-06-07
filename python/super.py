# Функція super() повертає проксі-об’єкт (тимчасовий об’єкт суперкласу), який дозволяє отримати доступ до методів базового класу.

class Animal(object):
    def __init__(self, animal_type):
        print('Animal Type:', animal_type)


class Mammal(Animal):
    def __init__(self):

        # Викликаємо суперклас
        super().__init__('Mammal')
        print('Mammals give birth directly')


dog = Mammal()

# Приклад №1: Функція super() з одинарним успадкуванням.
# У разі одинарного успадкування ми використовуємо функцію super() для посилання на базовий клас:


class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()

# Приклад №2: Функція super() з множинним успадкуванням.


class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.')


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog')


d = Dog()
print('')
bat = NonMarineMammal('Bat')


# Порядок виклику методів (скор. “MRO” від англ. “Method Resolution Order“) — це порядок,
# у якому методи повинні успадковуватися за наявності множинного успадкування.
# Ми можемо переглянути MRO за допомогою атрибуту __mro__.
# Ось як працює MRO:
# метод похідного класу завжди викликається раніше методу базового класу.
# У нашому прикладі клас Dog викликається перед NonMarineMammal або NoneWingedMammal.
# Ці два класи викликаються перед Mammal, який викликається перед Animal, а клас Animal викликається перед object;
#  якщо батьків декілька, наприклад, Dog(NonMarineMammal, NonWingedMammal),
# то методи NonMarineMammal викликаються першими, тому що цей клас з’являється першим.
