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

all_nums = [-5, 2, 0, 22, -12, 26, 92, -111]

absolute_nums = []
for num in all_nums:
    absolute_nums.append(abs(num))

print(absolute_nums)


# shorter_2

absolute_nums = [abs(num) for num in all_nums]
print(absolute_nums)
