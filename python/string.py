# Деякі приклади типу string (строка), строки Python є незмінними послідовностями,
# їх можна індексувати, нарізати та повторювати, як і будь-яку іншу послідовність.

city = 'Dnipro'  # Приклад звичайної строки
print(city)

fav_city = "My favorite city is"  # Приклад строки з декількох слів
print(fav_city, city)

# Приклад строки в декілька рядків """ """
place = """My favorite place is the beach.
I love the feeling of the soft sand
between my toes and the warm sun on my skin."""
print(place)

# or ''' '''

multiline = '''Line #1
Line #2
Line #3'''

print(multiline)
print(len(multiline))


# Визначення типу за допомогою type
print(type(city))

# Визначення кількості символів в строкі за допомогою функції len
city = 'Dnipro'
print(len(city))

# Визначення окремих символів строки (від 0 до останнього)
print(city[0])  # перший символ
print(city[3:6])  # символи з четвертого по шостий

# Заміна символів строки за допомогою методу replace
city = city.replace("p", "P")
print(city)
