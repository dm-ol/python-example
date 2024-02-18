# update() застосовується для додавання до множини рядка та словника.
# Метод розбиває рядок на окремі символи і додає їх до множини number1.
# Аналогічно він додає ключі словника до множини number2.
alphabet = 'odd'

number1 = {1, 3}
number2 = {2, 4}

number1.update(alphabet)
print('Set and strings:', number1)
# Set and strings: {1, 3, 'o', 'd'}

key_value = {'key': 1, 'lock': 2}

number2.update(key_value)
print('Set and dictionary keys:', number2)
# Set and dictionary keys: {'lock', 2, 4, 'key'}
