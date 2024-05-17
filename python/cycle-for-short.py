# Варіанти коротшого написання циклу for in

numbers = [12, 34, 1, 4, 4, 67, 37, 9, 0, 81]

# Original (list)

result = []
for number in numbers:
    if number > 5:
        result.append(number)
print(result)  # Prints [12, 34, 67, 37, 9, 81]

# Shorter (list)

result = [number for number in numbers if number > 5]
print(result)  # Prints [12, 34, 67, 37, 9, 81]


# Original_2 (list)

all_nums = [-5, 2, 0, 22, -12, 26, 92, -111]

absolute_nums = []
for num in all_nums:
    absolute_nums.append(abs(num))

print(absolute_nums)


# shorter_2 (list)

absolute_nums = [abs(num) for num in all_nums]
print(absolute_nums)


# Original_3 (set)

my_set = {1, 10, 15, 20}

new_set = set()

for val in my_set:
    new_set.add(val * val)

print(new_set)

# Shorter_3 (set)
new_set = {val * val for val in my_set}
print(new_set)


# Original_4 (dict)

my_scores = {
    'a': 22,
    'b': 12,
    'c': 5,
    'd': 9
}

scores = {}

for key, value in my_scores.items():
    scores[key] = value * 10

print(scores)

# Shorter_4 (dict)

scores = {key: value * 10 for key, value in my_scores.items()}
print(scores)
