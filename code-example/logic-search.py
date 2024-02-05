# Проста функція логічного пошуку значення в списку
list_1 = [2, 42, 13, 88, 36, 49, 114, 99, 41, 9, 63, 200]
found = False
print('Before', found)
for value in list_1 :
    if value == 88 :
        found = True
        print(found, value)
print('After', found)
