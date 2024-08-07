# Для обчислення розміру об'єкта ми можемо використовувати функцію getsizeof(object[, default]) із модуля sys.
# Оскільки в Python все є об'єктами, то і обчислити розмір пам'яті ми можемо в будь-якого об'єкта.

import sys
print(sys.getsizeof(5))

print(sys.getsizeof(range(0, 10000)))

print(sys.getsizeof([1, 2, 'c']))

# І хоча всі built-in (вбудовані) об'єкти повернуть правильний розмір,
# в загальному випадку це не повинно бути правильно для будь-яких об'єктів користувача.

# Аргумент default дозволяє визначити значення, яке буде повернене,
# якщо тип об'єкта не надає засоби для вилучення розміру та викличе TypeError.

# Функція getsizeof викликає метод __sizeof__ об'єкта та додає додаткові службові дані збирача сміття.
