# Вбудована функція, яка повертає число, округлене до N знаків з точністю після коми. 
import math # Імпортуємо модуль для ведення числа Пі
x = 358 / 47
print(x) # Повертає 7.617021276595745
print(round(x, 3)) # Повертає 7.617 - 3 знаки після коми
print(round(x, 2)) # Повертає 7.62 - 2 знаки після коми

pi = math.pi
print(pi) # Повертає 3.141592653589793
print(round(pi, 2)) # Повертає звичне всім 3.14
