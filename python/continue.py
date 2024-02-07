# continue ‒ поводиться так, ніби програма раптово дійшла до кінця тіла; починається виконання наступного оберту і негайно перевіряється умова.
print("\Інструкція continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Всередині циклу.", i)
print("За межами циклу.")

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
   number = int(input("Введіть число або наберіть -1 для завершення програми: "))

if counter:
   print("Найбільше число дорівнює", largest_number)
else:
   print("Ви не ввели жодного числа.")