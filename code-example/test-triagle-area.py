# Визначення площі трикутника
try: # Вводимо довжину сторін
    a = float(input("Довжина сторони 1:"))
    b = float(input("Довжина сторони 2:"))
    c = float(input("Довжина сторони 3:"))
except ValueError:
    print("Помилка: Будь ласка введіть числове значення.")
    quit()


def is_a_triangle(a, b, c): # Перевірка чи це трикутник
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    # Полупериметр
    s = (a + b + c) / 2
    # Визначення площі за формулою Герона
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
  
print("Площа трикутника дорівнює:", round(heron(a, b, c), 3)) # Вивід результату з округленням до 3 знаків після коми.
