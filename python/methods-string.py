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

# capitalize()– змінює всі літери рядка на великі
# center()– центрує рядок всередині поля відомої довжини
# count()– підраховує випадки появи заданого символу
# join()– об’єднує всі елементи кортежу/списку в один рядок
# lower()– перетворює всі літери рядка в малі літери
# lstrip()– видаляє білі символи з початку рядка
# replace()– замінює заданий підрядок іншим
# rfind()– знаходить підрядок, починаючи з кінця рядка
# rstrip()– видаляє кінцеві пробіли з кінця рядка
# split()– розбиває рядок на підрядок за допомогою заданого розділювача
# strip()– видаляє пробіли на початку та в кінці
# swapcase()– змінює регістр літер(нижній на верхній і навпаки)
# title()– першу літеру в кожному слові робить великою
# upper()– перетворює всі літери рядка у великі літери.
# endswith()– рядок закінчується заданим підрядком?
# isalnum()– рядок складається лише з букв і цифр?
# isalpha()– рядок складається лише з букв?
# islower()– рядок складається лише з малих літер?
# isspace()– рядок складається лише з пробілів?
# isupper()– рядок складається лише з великих літер?
# startswith()– чи починається рядок із заданого підрядка?


# Перевіримо деякі методи:

print(number.upper())  # BARK
print(number.lower())  # bark
print(number.title())  # Bark
print(number.capitalize())  # Bark
print(number.replace("B", "P"))  # ParK

# Метод center() створює копію вихідного рядка, намагаючись розташувати його всередині поля заданої ширини.

# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')

# Метод isalnum() перевіряє, чи рядок містить лише цифри або букви (літери)

# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())


# Метод join() виконує об’єднання – він очікує один аргумент як список; необхідно переконатися,
# що всі елементи списку є рядками – інакше метод викличе виняток TypeError ;
# усі елементи списку будуть об’єднані в один рядок, але рядок,
# з якого було викликано метод, використовується як роздільник , розміщений серед рядків;
# у результаті повертається новостворений рядок.

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))
