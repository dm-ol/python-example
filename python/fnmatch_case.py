# Метод fnmatch() перевіряє, чи ім'я файлу відповідає шаблонному рядку (він нечутливий до регістру).

# Зазвичай fnmatch() робить порівняння, використовуючи ті самі правила обліку регістру, що й ОС.

from fnmatch import fnmatch

fnmatch('foo.txt', '*,txt')  # True
fnmatch('foo.txt', '?oo. txt')  # True
fnmatch('Dat45.csv', 'Dat [0-9]*')  # True
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo-py']
[name for name in names if fnmatch(name, 'Dat*,csv')]
# ['Dat1.csv', 'Dat2. csv']

# Метод fnmatchcase() робить те саме, тільки він чутливий до регістру.
