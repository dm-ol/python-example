# Приклад функції для знаходження найбільшого числа
largest = None
print("First largest number:", largest)
for number in [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]:
    if largest is None:
        largest = number
    elif largest > number:
        largest = number
    print("Number from list:", number, "Last largest number:", largest)
print("Largest number from the list:", largest)
