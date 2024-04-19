# Для створення хеш-значень у Python існує зручний модуль hashlib, який реалізує
# спільний інтерфейс для ряду популярних хеш-функцій і може використовувати
# функції, що доступні в системі і надаються зі встановленим OpenSSL. https://docs.python.org/3/library/hashlib.html

import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()

m.hexdigest()
print(m)
