# Функція reversed() обчислює інверсію вказаного об’єкта послідовності та повертає її у вигляді списку.

seq_string = 'Python'

# Виводимо рядок "задом наперед"
print(list(reversed(seq_string)))

# Функція reversed() у Python із вбудованими об’єктами послідовності

seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# Інверсія кортежу
print(list(reversed(seq_tuple)))

seq_range = range(5, 9)

# Інверсія діапазону
print(list(reversed(seq_range)))

seq_list = [1, 2, 4, 3, 5]

# Інверсія списку
print(list(reversed(seq_list)))


# Функція reversed() в Python з користувацькими об’єктами

class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)


v = Vowels()

# Інверсія користувацького об'єкта v
print(list(reversed(v)))
