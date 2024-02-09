# В Python є спеціальний метод, який може розширити область видимості змінної таким чином,
# щоб вона входила до тіла функції (навіть якщо ви хочете не тільки прочитати значення,
# але й модифікувати його). Такий ефект спричиняє ключове слово global:
def my_function():
   global var
   var = 2
   print("Чи знаю я цю змінну?", var)

var = 1
my_function()
print(var)

# or

var = 2
print(var)    # виведе: 2
 
def return_var():
    global var
    var = 5
    return var
 
print(return_var())    # виведе: 5
print(var)    # виведе: 5
 
