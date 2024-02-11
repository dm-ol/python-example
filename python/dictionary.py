# Словник — ще одна структура даних Python. Він не є послідовним типом
# (але може бути легко адаптований до обробки як послідовність) і є змінним.
# Словник — це набір пар ключ-значення і береться у фігурні дужки.
# Самі пари відокремлюються комами, а ключі та значення ‒ двокрапкою.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {} 
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# Кожен ключ повинен бути унікальним ‒ не можна мати більше одного ключа з тим самим значенням.
# Ключем може бути будь-який незмінний тип об'єкта: це може бути число (ціле або з рухомою крапкою),
# або навіть рядок, але не список.

# Якщо ви хочете отримати будь-яке зі значень, вам потрібно вказати дійсне значення ключа.
# Ключі чутливі до регістру. Якщо ключ є рядком, то його необхідно вказувати як рядок.
 
print(dictionary['cat'])
print(phone_numbers['Suzy'])

# Висячий відступ, приклад 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# приклад 2:
phone_numbers = {
                'boss': 5551234567,
                'Suzy': 22657854310
}
 

 
