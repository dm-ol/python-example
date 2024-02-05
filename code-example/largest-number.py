# Приклад функції для знаходження найбільшого числа 
largest = 1
print("First largest number:", largest)
for number in [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]:
    if number > largest:
        largest = number
    print("Number from list:", number, "Last largest number:", largest)
print("Largest number from the list:", largest)
    