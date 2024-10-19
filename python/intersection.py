# Метод intersection() повертає набір, який містить схожість між двома чи більше наборами.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)  # ['apple']

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)
print(result)  # ['c']

# Набір, що повертається, містить тільки елементи, які існують в обох наборах або у всіх наборах, якщо порівняння виконується більш, ніж з двома наборами.
