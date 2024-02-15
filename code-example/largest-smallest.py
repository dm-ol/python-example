# Тестове завдання. Напишіть програму, яка просить користувача вводити цілі числа допоки користувач не зазначить «готово» (“done”).
# Після введення «готово» (“done”), виведіть найбільше та найменше з введених чисел. Якщо користувач вводить некоректне число,
# обробіть його за допомогою try / except, виведіть на екран відповідне повідомлення, та проігноруйте це число.
largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num.lower() == "done":
        break

    try:
        fnum = int(num)
    except ValueError:
        print("Invalid input")
        continue

    if largest is None or fnum > largest:
        largest = fnum

    if smallest is None or fnum < smallest:
        smallest = fnum

print("Maximum is", largest)
print("Minimum is", smallest)
