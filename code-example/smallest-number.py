# Приклад функції для знаходження найменшого числа 
smallest = None
print("First smallest number:", smallest)
for number in [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    print("Number from list:", number, "Last smallest number:", smallest)
print("Smallest number from the list:", smallest)
    