# Створіть нову функцію на два параметри з ім'ям merge_list_to_dict.
# Функція повинна об'єднувати два списки за допомогою zip(),
# а потім конвертувати в словник і повернути його із функції.

def merge_list_to_dict(list_1, list_2):
    sum_dict = dict(zip(list_1, list_2))
    return (sum_dict)

# Створіть два списки, які будуть використовуватись як аргументи


brand = ["Audi", "Alfa Romeo", "BMW", "Ferrari", "Mercedes-Benz"]
model = ["R8", "Julia", "850", "FXX", "SLR"]

# Визвіть функцію і передайте їй аргументи та виведіть результат на екран

cars = merge_list_to_dict(brand, model)
print(cars)
