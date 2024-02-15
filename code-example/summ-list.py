# Приклад функції для знаходження суми чісел у списку
list_sum = 0
for number in [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]:
    list_sum = list_sum + number
    print("Number from list:", number, "Last list summ:", list_sum)
print("Largest summ from the list:", list_sum)

# or

my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
total = 0
# змінна i приймає значення 0, 1, 2, 3 та 4, потім індексує список, вибираючи наступний елемент: перший, другий, третій, четвертий і п'ятий
# використовується функція len() для визначення точної кількості елементів списку
for i in range(len(my_list)):
    total = total + my_list[i]  # total += my_list[i]

print(total)

# or

my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
total = 0

for i in my_list:
    total = total + i  # total += i

print(total)

# or

my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
total = sum(my_list)
print(total)
