# Метод extend() використовується для додавання всіх елементів одного списку до іншого. Наприклад:

prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)

even_numbers = [4, 6, 8]
print("List2:", even_numbers)

# Об'єднання двох списків
prime_numbers.extend(even_numbers)

print("List after append:", prime_numbers)
