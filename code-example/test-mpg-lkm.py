# Витрата палива автомобілем може бути оцінена багатьма різними способами. Наприклад,
# в Європі вона подається як кількість палива, що витрачається на 100 кілометрів пробігу.
# У США вона вимірюється в милях, які проїжджає автомобіль, витрачаючи один галон пального.
# Ваше завдання - написати пару функцій, які переводять l/100km в mpg, і навпаки.
# 1 американська миля = 1609,344 метра;
# 1 американський галон = 3,785411784 літра.

def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
