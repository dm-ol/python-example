# Функція slice() повертає об’єкт зрізу, який використовується для
# зрізу будь-якої послідовності (рядка, кортежу, списку, діапазону).

# Приклад №1: Створення об’єкта зрізу

# Містить індекси (0, 1, 2)
result1 = slice(3)
print(result1)

# Містить індекси (1, 3)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2))

# Приклад №2: Отримання підрядка через об’єкт зрізу

# Програма для отримання підрядка із заданого рядка

py_string = 'Python'

# stop = 3
# Містить індекси 0, 1 та 2
slice_object = slice(3)
print(py_string[slice_object])

# start = 1, stop = 6, step = 2
# Містить індекси 1, 3 та 5
slice_object = slice(1, 6, 2)
print(py_string[slice_object])

# Приклад №3: Отримання підрядка за допомогою від’ємного індексу

py_string = 'Python'

# start = -1, stop = -4, step = -1
# Містить індекси -1, -2 та -3
slice_object = slice(-1, -4, -1)

print(py_string[slice_object])

# Приклад №4: Отримання підсписку та підкортежу

py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# Містить індекси 0, 1 та 2
slice_object = slice(3)
print(py_list[slice_object])

# Містить індекси 1 та 3
slice_object = slice(1, 5, 2)
print(py_tuple[slice_object])
