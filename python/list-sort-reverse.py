# Якщо ви хочете, щоб Python відсортував ваш список, ви можете зробити це так:
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
my_list.sort()
print(my_list)

# При бажанні можна сортувати самостійно:
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]  # list to sort
swapped = True  # Це невеличка хитрість, щоб увійти в цикл while.

while swapped:
    swapped = False  # поки немає обмінів
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # відбувся обмін!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

# Існує також метод списку з назвою reverse(), який можна використовувати для зворотного розташування елементів списку, наприклад:
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
print(my_list)

my_list.reverse()
print(my_list)  # виведе: [200, 63, 9, 41, 99, 114, 49, 36, 88, 13, 42, 2]

# Можна спочатку відсортувати, а потім розташувати зворотньо:
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
print(my_list)
my_list.sort()
my_list.reverse()
print(my_list)

# або

my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
print(my_list)
my_list.sort(reverse=True)
print(my_list)
