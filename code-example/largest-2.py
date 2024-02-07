# Збережіть поточне найбільше число тут. Використаємо None
largest = None

# Введіть перше число.
number = int(input("Введіть число або -1, щоб зупинити: "))
 
# Якщо число не дорівнює -1, продовжуйте.
while number != -1:
    # Чи є число більшим за largest_number?
    if largest is None:
        largest = number
    if number > largest:
        # Так, оновити largest_number.
        largest_number = number
    # Введіть наступне число.
    number = int(input("Введіть число або -1, щоб зупинити: "))
 
# Виведіть найбільше число.
print("Найбільше число це:", largest_number)
 
