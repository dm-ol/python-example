# Скрипт для створення резервної копії файлів

# Імпортуємо модулі

import shutil
import datetime

# Вказуємо шляхи
source = "Path to source directory"

backup_folder = "Path to backup directory"

# Вказуємо таймштамп для бекапа і його ім'я
timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

backup_name = f'backup_{timestamp}'

# Робимо бекап
shutil.copytree(source, f'{backup_folder}/{backup_name}')
