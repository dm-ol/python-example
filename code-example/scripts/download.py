# Скрипт для скачування файлів за URL

import requests

url = 'file_URL'

destination = 'Path for save'

response = requests.get(url)

with open(destination, 'wb') as file:

    file.write(response.content)
