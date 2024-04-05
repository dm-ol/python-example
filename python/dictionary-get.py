# Метод get() повертає значення елементу з вказаним ключем.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.get("model")

print(x)

# Спроба повернути значення елемента, якого не існує:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.get("price", 15000)

print(x)
