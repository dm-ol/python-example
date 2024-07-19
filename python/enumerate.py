# Функція enumerate() додає лічильник до ітерованого об’єкта та повертає його.
# Об’єкт, що повертається — це перелічувальний об’єкт.
# Ми можемо конвертувати перелічувальні об’єкти в список та кортеж, використовуючи функції list() та tuple() відповідно.

# Синтаксис функції enumerate(): enumerate(iterable, start=0)
# Функція enumerate() приймає два параметри:
#    iterable — послідовність, ітератор або об’єкти, які підтримують ітерацію;
#    start (не обов’язково) — початок відліку. Якщо цей параметр не вказано, то в якості значення за замовчуванням використовується 0.

languages = ['Python', 'Java', 'JavaScript']

enumerate_languages = enumerate(languages)

# Конвертуємо перелічувальний об'єкт в список
print(list(enumerate_languages))

# Робота функції enumerate()

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# Перетворюємо на список
print(list(enumerateGrocery))

# Змінюємо лічильник, вказаний за замовчуванням
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))


# Цикл і перелічувальний об’єкт

grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
    print(item)

print()

for count, item in enumerate(grocery):
    print(count, item)

print()

# Змінюємо стартове значення, вказане за замовчуванням
for count, item in enumerate(grocery, 100):
    print(count, item)
