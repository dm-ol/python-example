# Метод — це по суті функція, яка "закріплена" за певним об'єктом і яка виконує певні дії над цим об'єктом.
# Записується це наступним чином: об'єкт чи посилання на нього, далі ставиться крапка, і після крапки метод об'єкта:
# object.method()

#  Перевіряємо список доступних атрібутів для строки, в тому числі медоди:
print("dir для строки")
number = 'BarK'
# Отримуємо список: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
print(dir(number))
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
# 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
# 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
# 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
# 'title', 'translate', 'upper', 'zfill']

# Перевіримо деякі методи:

print(number.upper())  # BARK
print(number.lower())  # bark
print(number.title())  # Bark
print(number.capitalize())  # Bark
print(number.replace("B", "P"))  # ParK

# Метод center() створює копію вихідного рядка, намагаючись розташувати його всередині поля заданої ширини.

# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
