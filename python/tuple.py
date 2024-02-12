# tuple (кортеж) -  це тип незмінної послідовності. Він може поводитися як список, але не може 
# бути змінений в процесі виконання. Перша і найбільш очевидна відмінність списків від кортежів 
# полягає в синтаксисі, який використовується для їх створення ‒ кортежі створюють за допомогою
# круглих дужок, в той час як списки ‒ за допомогою квадратних дужок, хоча також можна створити
# кортеж просто з набору значень, розділених комами.
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
 
print(tuple_1)
print(tuple_2)
 
# Якщо ви хочете створити одноелементний кортеж, ви повинні враховувати той факт, 
# що з синтаксичних міркувань (кортеж повинен відрізнятися від звичайного, 
# одиночного значення), ви повинні закінчити значення комою:
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

# Приклади використання
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000) # можна об'єднувати кортежі між собою
t2 = my_tuple * 3 # можна перемножувати кортежі так само як і списки

print(len(t2)) # приймає кортежі і повертає кількість елементів, що містяться всередині
print(t1)
print(t2)
print(10 in my_tuple) # Перевіряє наявність 10 в кортежі
print(-10 not in my_tuple) # Перевіряє відсутність -10 в кортежі

# елементами кортежу можуть бути змінні, а не тільки літерали. Більше того, вони можуть
# бути виразами, якщо стоять у правій частині оператора присвоювання.
var = 123

t1 = (3, "var", 44, "car", var)

print(t1)

#Ви можете перебирати елементи кортежу в циклі (Приклад 1),
# перевіряти наявність (відсутність) певного елемента в кортежі (Приклад 2),
# використовувати функцію len() для перевірки кількості елементів в кортежі (Приклад 3),
# або навіть об'єднувати/перемножувати кортежі (Приклад 4)
# приклад 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)
 
# приклад 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)
 
# приклад 3
tuple_3 = (1, 2, 3, 4)
print(len(tuple_3))
print(5 not in tuple_3)
# приклад 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2
 
print(tuple_4)
print(tuple_5)
 
# Створити кортеж можна також за допомогою вбудованої функції Python з назвою tuple().
# Це особливо корисно, коли потрібно перетворити певний повторюваний об'єкт (наприклад, список, діапазон, рядок і т.д.) в кортеж:
my_tuple = tuple((1, 2, "string"))
print(my_tuple)
 
my_list = [2, 4, 6]
print(my_list) # виведе: [2, 4, 6]
print(type(my_list)) # виведе: <class 'list'>
tup = tuple(my_list)
print(tup) # виходи: (2, 4, 6)
print(type(tup)) # виведе: <class 'tuple'>
 

 
