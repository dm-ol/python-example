# У функції відбувається піднесення кожного елемента списку до квадрату. Вона не змінює
# оригінальний список, а лише створює новий список, в якому всі елементи піднесені до квадрату.
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list
 
foo = [1, 2, 3, 4, 5]
print(list_updater(foo))
 
#  Якщо ви хочете змінити оригінальний список, ви можете зробити це без створення нового списку.
def list_updater(lst):
    for i in range(len(lst)):
        lst[i] **= 2

foo = [1, 2, 3, 4, 5]
list_updater(foo)
print(foo)
