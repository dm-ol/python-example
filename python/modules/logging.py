# Модуль logging визначає функції та класи, які реалізують гнучку систему реєстрації подій для додатків та бібліотек.
# Ключова перевага наявності API-інтерфейсу ведення журналу в тому, що всі модулі Python можуть брати участь у веденні журналу.

# Таким чином, журнал вашого додатка може включати твої власні повідомлення, інтегровані з повідомленнями зі сторонніх модулів.

import logging
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s % (name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.debug('this is a %s test', 'debug')
