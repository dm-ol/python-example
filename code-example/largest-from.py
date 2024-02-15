# Зчитайте три числа
try:
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    number3 = int(input("Введіть третє число: "))
except ValueError:
    print("Помилка: Будь ласка введіть числове значення.")
    quit()
# Тимчасово припустимо, що перше число
# є найбільшим.
# Ми незабаром це перевіримо.
largest_number = number1

# Перевіряємо чи друге число більше поточного largest_number
# і оновлюємо largest_number, якщо потрібно.
if number2 > largest_number:
    largest_number = number2

# Перевіряємо, чи третє число більше поточного largest_number
# і оновлюємо largest_number, якщо потрібно.
if number3 > largest_number:
    largest_number = number3

# Виведіть результат
print("Найбільше число це:", largest_number)
