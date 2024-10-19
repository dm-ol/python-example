# Метод difference() повертає набір, що містить різницю між двома наборами.

# Набір, що повертається, містить елементи, які існують тільки в першому наборі, а не в обох.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
z1 = y.difference(x)

print(z)  # ['cherry', 'banana']
print(z1)  # ['google', 'microsoft']
