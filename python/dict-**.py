# Розпаковка та об'єднання словників за допомогою оператора **

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car_price = {
    **car,  # Беремо словник cars та доповнюємо його новим ключем
    "price": 120000
}

print(car_price)  # Новий словник з новим ключем Price

print(car)  # Перший словник без змін

# Об'єднання словників

car_3_inf = {
    "brand": "Chevrolet",
    "model": "Corvette",
    "year": 1968
}

car_3_set = {
    "color": "Red",
    "price": 80000
}

car_3 = {
    **car_3_inf,
    **car_3_set
}

print(car_3)

# Варіант перезапису ключа в словнику

car_2 = {
    "brand": "Ferrari",
    "model": "F50",
    "year": 1995,
    "price": 500000
}

car_2_price = {
    **car_2,  # Беремо словник car та змінюємо значення ключа price
    "price": 800000
}

print(car_2_price)
print(car_2)
