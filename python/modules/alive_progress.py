# Модуль прогрес бару alive-progress є багатофункціональним, простим у використанні і з безліччю вбудованих стилів.
# Більше того, ви можете легко створювати власні ефекти. Попередньо встановіть за допомогою pip install alive-progress.

from alive_progress import alive_bar
import time

for x in 3000, 2000, 1000, 0:
    with alive_bar(total=x) as bar:
        for i in range(3000):
            time.sleep(.002)
            bar()
