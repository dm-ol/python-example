# Функція locals() повертає словник з усіма локальними змінними та символами поточної програми.

print(locals())

# Приклад №1: Функція locals() в Python


class local:
    l = 50
    # Локальні об'єкти всередині класу
    print('\nlocals() value inside class\n', locals())


# Приклад №2: Функція locals() для зміни значень

def localsPresent():
    present = True
    print(present)
    locals()['present'] = False
    print(present)


localsPresent()
