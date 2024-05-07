# Розпаковка списка (list)

my_cars = ["Audi", "BMW", "Ferrari", "Mclaren"]

car_1, car_2, car_3, car_4 = my_cars

print(car_1)
print(car_2)
print(car_3)
print(car_4)


# Розпаковка кортежа (tuple)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Групування з 3-го до останнього
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Групування з 2-го по передостанній
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Розпаковка списка (list) для функції

my_moto = ["Honda", "NC 750X"]


def moto_info(manuf, model):
    if not model:
        return f"{manuf} is best motorcicle, but no model"
    return f"{manuf} is best manufacturer, especially {model}"


print(moto_info(*my_moto))
