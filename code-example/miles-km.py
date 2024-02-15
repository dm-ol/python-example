# Приклад простого конвертеру миля-кілометр
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.609344
kilometers_to_miles = kilometers / 1.609344

print(miles, "миль", round(miles_to_kilometers, 3), "кілометрів")
print(kilometers, "кілометрів є", round(kilometers_to_miles, 3), "миль")
