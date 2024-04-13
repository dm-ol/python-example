# Функція id() повертає унікальне ціле число (ідентифікатор) переданого об’єкта аргументу.
my_list = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
print(id(my_list))

kilometers = 12.25
print(id(kilometers))


# id списку (змінюваний об'єкт)

list_1 = [4, 8, 12, 24, 76, 100]

print("ID: ", id(list_1))  # id списку list_1
print("List: ", list_1)

list_1.append(202)  # Додаємо число до списку

print("ID: ", id(list_1))  # id списку list_1 після додання ще одного числа
print("List: ", list_1)

# id строки (незмінюваний об'єкт)

string_1 = "abc"

print("ID: ", id(string_1))  # id строки string_1
print("String_1: ", string_1)

string_2 = string_1

print("ID: ", id(string_2))  # id строки string_2
print("String_2: ", string_2)

string_2 += "wsx"

# id строки string_2 після додавання нових об'єктів
print("ID: ", id(string_2))
print("String_2+add: ", string_2)
