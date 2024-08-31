# Методи в Python
# Функція, визначена всередині класу, називається методом.

# Створюємо клас
class Room:
    length = 0.0
    width = 0.0

    # Метод обчислення площі
    def calculate_area(self):
        print("Area of Room =", self.length * self.width)


# Створюємо об'єкт класу Room
study_room = Room()

# Надаємо нові значення всім атрибутам об'єкта
study_room.length = 42.5
study_room.width = 30.8

# Отримуємо доступ до методу всередині класу
study_room.calculate_area()
# Результат:

# Area of Room = 1309.0

# Тут ми створили клас Room з атрибутами: length та width; та методом calculate_area().
# Потім ми створили об’єкт study_room класу Room та використали цей об’єкт для присвоєння
# значень атрибутам length та width. Зверніть увагу, що ми також використали цей об’єкт
# для виклику методу всередині класу за допомогою оператора .:

study_room.calculate_area()
