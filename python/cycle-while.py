# Цикл while використовується для виконання блоку коду доти, доки не буде досягнуто певної умови.
# Цикл while виконує оператор або набір операторів до тих пір, поки задана логічна умова є істинною.
# Використовуються для dict, list, tuple, str, set, range.
# Алгоритм дій:
#   Спочатку цикл while обробляє умову.
#   Якщо умова обчислюється як True, то виконується код всередині циклу while.
#   Потім умова повторно обробляється. Цей процес триває доти, доки умова не стане False.
#   Якщо умова обчислюється як False, цикл завершує своє виконання.

# У цій програмі ми виводимо числа від 1 до 5

# Ініціалізація змінних
i = 1
n = 5

# Цикл while з i = 1 до 5
while i <= n:
    print(i)
    i = i + 1


# У цій програмі ми обчислюємо суму чисел доти,
# доки користувач не введе 0

total = 0

number = int(input('Enter a number: '))

# Додаємо числа, доки number не дорівнюватиме 0
while number != 0:
    total += number  # total = total + number

    # Запитуємо користувацький ввід
    number = int(input('Enter a number: '))


print('total =', total)


# Приклад нескінченного циклу:
# while True:
#     print("Застряг у нескінченному циклі.")

# Приклад 1
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# Приклад 2 простого циклу
n = 100
while n > 1:
    print(n)
    n = n - 1
print("Рівно одиниця:", n)

# У Python цикл while може мати необов’язковий блок else, який виконуватиметься після того, як умова циклу стане False.

counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

# Цикл while з break

while True:
    answer = input("Enter yes or no: ")
    if answer == "no":
        break
