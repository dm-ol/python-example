# Приклад функції для знаходження суми чісел у списку
list_sum = 0
for number in [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]:
    list_sum = list_sum + number
    print("Number from list:", number, "Last list summ:", list_sum)
print("Largest summ from the list:", list_sum)
    