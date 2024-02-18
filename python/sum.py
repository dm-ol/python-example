# sum() додає елементи об'єкта, що ітерується, і повертає суму.
# За потреби можна вказати параметр start. Це значення додається до суми елементів ітерації.
numbers = [2.5, 3, 4, -5]

numbers_sum = sum(numbers)
print(numbers_sum)  # 4.5

numbers_sum = sum(numbers, 10)
print(numbers_sum)  # 14.5
