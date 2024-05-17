# continue ‒ поводиться так, ніби програма раптово дійшла до кінця тіла; починається виконання наступного оберту і негайно перевіряється умова.
import random
print("\Інструкція continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Всередині циклу.", i)
print("За межами циклу.")

# Написати програму з циклом for та оператором continue. Програма повинна перебрати послідовність цифр,
# замінити кожен 0 на x і вивести змінений рядок на екран.
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

# Ще один приклад continue
largest_number = -99999999
counter = 0

number = int(input("Введіть число або наберіть -1 для завершення програми: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(
        input("Введіть число або наберіть -1 для завершення програми: "))

if counter:
    print("Найбільше число дорівнює", largest_number)
else:
    print("Ви не ввели жодного числа.")


# Ще один приклад роботи continue


random_num = random.randint(1, 11)
while True:
    num = int(input("Enter the number from 1 to 10: "))
    if num != random_num:
        print("Try again!")
        continue
    print("Yes, this is ", random_num)
    break
