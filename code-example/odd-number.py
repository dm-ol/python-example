# Створіть цикл for, який рахує від 0 до 10 і виводить на екран непарні числа.
for i in range(0, 11):
    if i % 2 != 0:
        print(i)
        
# or
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1