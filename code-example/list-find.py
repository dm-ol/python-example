# Тепер давайте знайдемо місце розташування певного елемента в списку:
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
to_find = 99
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Елемент знайдено за індексом", i)
else:
    print("відсутній")
    
# Доопрацюємо трохи:
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
try:
    to_find = int(input("Введіть число, яке потрібно знайти: "))
except ValueError:
    print("Помилка: Будь ласка введіть числове значення.")
    quit()
    
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Елемент знайдено за індексом", i)
else:
    print("відсутній")
 
