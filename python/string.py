# Деякі приклади типу string (строка)

city = 'Dnipro'  # Приклад звичайної строки
print(city)

fav_city = "My favorite city is"  # Приклад строки з декількох слів
print(fav_city, city)

# Приклад строки в декілька рядків
place = """My favorite place is the beach.
I love the feeling of the soft sand
between my toes and the warm sun on my skin."""
print(place)

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
