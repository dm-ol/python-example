# Варіанти коротшого написання циклу for in

numbers = [12, 34, 1, 4, 4, 67, 37, 9, 0, 81]

# Original

result = []
for number in numbers:
    if number > 5:
        result.append(number)
print(result)  # Prints [12, 34, 67, 37, 9, 81]

# Shorter

result = [number for number in numbers if number > 5]
print(result)  # Prints [12, 34, 67, 37, 9, 81]


# Original_2
