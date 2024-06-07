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
