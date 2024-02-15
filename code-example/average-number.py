# Приклад функції для знаходження середнього значення в списку
list_sum = 0
item = 0
for number in [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]:
    list_sum = list_sum + number
    item = item + 1
average = list_sum / item
print("Largest summ from the list:", list_sum)
print("Number of items in the list:", item)
print("Average value in the list:", average)
# або просто
print("Average value in the list:", list_sum / item)
