# break ‒ негайний вихід з циклу, безумовне завершення роботи циклу; програма починає виконувати найближчу інструкцію після тіла циклу
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')

# Скласти програму з циклом for та оператором break. Програма повинна перебирати символи в адресі електронної пошти,
# виведети з циклу при досягненні символу @ і виводити частину до @ в одному рядку
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Ще один приклад break
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

# Ще один приклад break
print("Інструкція break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Всередині циклу.", i)
print("За межами циклу.")

# Ще один приклад break. Завершує роботу циклу.
largest_number = -99999999
counter = 0

while True:
     number = int(input("Введіть число або введіть -1 для завершення програми: "))
     if number == -1:
         break
     counter += 1
     if number > largest_number:
       largest_number = number

if counter != 0:
    print("Найбільше число", largest_number)
else:
    print("Ви не ввели жодного числа.")

