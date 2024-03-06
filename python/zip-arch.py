from zipfile import ZipFile

# вказуємо назву архіву
file_name = 'archive.zip'

# відкриваємо файл у режимі читання
with ZipFile(file_name, 'r') as zip:

    # дивимося вміст
    zip.printdir()

    # вилучаємо файли
    zip.extractall()
