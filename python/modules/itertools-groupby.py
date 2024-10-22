# Метод groupby() в itertools спершу проходить через ітерацію і групує значення на основі певного ключа. Потім він повертає ітератор (потік кортежів).

import itertools

a_list = [("Animal", "cat"),
          ("Animal", "dog"),
          ("Bird", "peacock"),
          ("Bird", "pigeon")]

an_iterator = itertools.groupby(a_list, lambda x: x[0])
for key, group in an_iterator:
    key_and_group = {key: list(group)}
    print(key_and_group)

# {'Animal': [('Animal', 'cat'), ('Animal', 'dog')]}
# {'Bird': [('Bird', 'peacock'), ('Bird', 'pigeon')]}

# Оскільки groupby() перевіряє лише послідовні елементи, відсутність початкового сортування не призведе до угруповання записів так, як ви хочете.
