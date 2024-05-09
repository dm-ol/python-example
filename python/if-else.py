# Умовні інструкції if-else-elif

# Оператор if використовується для виконання блоку коду лише за умови дотримання конкретної умови.

number = 15

# Перевіряємо, чи більше 0 значення змінної number
if number > 0:
    print('Number is positive.')

print('The if statement is easy')


# Оператор if може мати необов’язкову умову else.
# Оператор if...else використовується для виконання блоку коду серед двох альтернатив.

number_2 = 15

if number_2 > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement is always executed')

# Однак, якщо потрібно зробити вибір у випадках, коли альтернатив більше ніж дві, то використовується оператор if...elif...else.

number_3 = 0

if number_3 > 0:
    print("Positive number")

elif number_3 == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')

# Ми також можемо використовувати один оператор if всередині іншого оператора if. Це називається вкладеним оператором if.

number_4 = 10

# Зовнішній оператор if
if (number_4 >= 0):
    # Внутрішній оператор if
    if number_4 == 0:
        print('Number is 0')

    # Внутрішній оператор else
    else:
        print('Number is positive')

# Зовнішній оператор else
else:
    print('Number is negative')
