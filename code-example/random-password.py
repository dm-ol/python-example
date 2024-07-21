# Щоб створити рандомний пароль, можна скористатися символами, наданими у модулі string.
# punctuation відповідає за знаки пунктуації, ascii letters — за літери,
# а digits — за цифри. Далі об'єднуємо всі символи через symbols.
# Використовуйте random.SystemRandom для створення пароля.

import random

from string import punctuation, ascii_letters, digits

symbols = ascii_letters + digits + punctuation

secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbols) for i in range(16))
print(password)
