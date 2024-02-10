# Просто приклад факторіалу
import math
y = math.factorial(5)
print(y)

# Приклад обчислення факторіалу у діапазоні від 0 до 5, за допомогою функцій
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6):  # тестування
    print(n, factorial_function(n))
    
#Рекурсивна реалізація функції факторіала.
def factorial(n):
    if n == 1:    # Базовий випадок (умова завершення.)
        return 1
    else:
        return n * factorial(n - 1)
 
 
print(factorial(5)) # 5 * 4 * 3 * 2 * 1 = 120

 
