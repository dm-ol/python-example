hat_list = [1, 2, 3, 4, 5] # Це початковий список чисел, прихованих у капелюсі.

# Крок 1: написати рядок коду, який пропонує користувачеві
# замінити середнє число на ціле число, введене користувачем.
hat_list[2] = int(input("Введіть число: "))

# Крок 2: написати рядок коду, який видаляє останній елемент зі списку.
del hat_list[-1]

# Крок 3: написати рядок коду, що виводить довжину списку.
print("Довжина списку:", len(hat_list))
print(hat_list)