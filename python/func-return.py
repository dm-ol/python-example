# Щоб змусити функції повернути значення (але не тільки для цього) використовується інструкція return.
# Інструкція return має два різних варіанти ‒ розглянемо їх окремо.

# 1) return без повернення результату
def happy_new_year(wishes = True):
    print("Три...")
    print("Два...")
    print("Один...")
    if not wishes:
        return
 
    print("Щасливого Нового року!")
 
happy_new_year() 
# or
happy_new_year(False) # виводить без print("Щасливого Нового року!")

# 2) return з поверненням результату
def boring_function():
    return 123
 
x = boring_function()
 
print("Функція boring_function повернула свій результат. Він:", x)
 
