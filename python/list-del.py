# інструкція del здатна видаляти один елемент списку за раз
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
del my_list[1] # видаляє елемент № 2
del my_list[4] # видаляє елемент № 5
print(my_list)

# Описана раніше інструкція del здатна видаляти не тільки один елемент списку за раз ‒ вона може видаляти зрізи:
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
del my_list[1:2] # видаляє елементи з 2 по 3
del my_list[4:6] # видаляє елементи з 5 по 7
print(my_list)

# Також можливе видалення всіх елементів одночасно:
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
del my_list[:]
print(my_list) # виведе пустий список

# В цьому випадку буде помилка, бо видаляється сам список, а не його зміст.
my_list = [10, 8, 6, 4, 2]
del my_list
# print(my_list)

# Також можливе видалення всіх елементів одночасно:
my_num = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
my_num.clear()
print(my_num)
 
