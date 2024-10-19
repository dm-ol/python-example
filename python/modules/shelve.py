# Вбудований модуль shelve дозволяє зберігати та читати довільні дані.
# Таким чином можна зберігати будь-які Python об'єкти для подальшого використання.

# Доступ до даних — за допомогою ключів, як і зі словниками.
# А метод shelve.open підтримує протокол контекстного менеджера (можна викликати метод close).

import shelve

# запис даних
with shelve.open('data') as shelf:
    shelf['key'] = {'int': 7, 'float': 12.5, 'string': 'something'}

# читання даних
with shelve.open('data') as shelf:
    print(shelf['key'])

# Output: ('int': 7, 'float': 12.5, 'string': 'something'}

# В документації заявляють, що така БД є "надійною".
# Але враховуючи, що shelve написаний на pickle, його варто використовувати лише у зовсім маленьких проектах.
