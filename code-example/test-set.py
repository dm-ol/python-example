# Створіть набір (set) з декількох елементів типу int
set_1 = {42, 12, 3, 92, 50, 25, 48, 10, 76}
print("First set: ", set_1)

# Додайте в нього ще один елемент
set_1.add(32)
print("First set, add number: ", set_1)

# Створіть ще один набір (set) з декількох елементів типу int, деякі повинні бути як в першому
set_2 = {12, 95, 50, 28, 64, 32, 1, 17, 10}
print("Second set:", set_2)

# Знайдіть спільні елементи двох наборів і запишіть їх в новий набір

set_3 = set_1.intersection(set_2)
print("Third set: ", set_3)

# Конвертуйте новий набір у список і виведіть його у термінал

list_1 = list(set_3)
print("Shared list: ", list_1)
