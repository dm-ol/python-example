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

# 2) return з поверненням результату. Результат функції можна легко призначити змінній
def boring_function():
    return 123
 
x = boring_function()

# або

print("Функція boring_function повернула свій результат. Він:", x)

def wishes():
    return "З Днем народження!"
 
w = wishes()
print(w)    # виведе: З Днем народження!

# Подивіться на різницю в результатах у наступних двох прикладах: 
# приклад 1
def wishes():
    print("Мої побажання")
    return "З Днем народження"
 
wishes() # виведе: Мої побажання
 
 
# приклад 2
def wishes():
    print("Мої побажання")
    return "З Днем народження"
 
print(wishes())
 
# виведе: Мої побажання
# З Днем народження
 