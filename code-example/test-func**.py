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


# Створіть функцію update_car_info, у якій всі іменовані аргументи будуть об'єднуватись
# у словник car. Додайте в словник новий ключ is_available з значенням True та поверніть
# із функції змінений словник.

def update_car_info(**car):
    car['is_available'] = True
    return car


# Додаєм аргументи з ключовими словами
car_info = update_car_info(brand='Audi', price=80000)
print(car_info)
