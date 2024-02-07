# Тестове завдання. Ваша програма повинна попросити користувача ввести слово;
# використовувати user_word = user_word.upper() для перетворення введеного 
# користувачем слова у верхній регістр; за допомогою умовного виконання та оператора continue 
# "з'їсти" # з введеного слова наступні голосні A, E, I, O, U; 
# вивести на екран нез'їдені літери, кожну в окремому рядку.
user_word = input("Введіть слово: ")
user_word = user_word.upper()

vowels = ['A', 'E', 'I', 'O', 'U']

for letter in user_word:
    if letter in vowels:
        continue
    print(letter)
    
    
# Ваше завдання тут ще більш особливе, ніж раніше: ви повинні переробити (потворного) пожирача
# голосних з попередньої лабораторної та створити кращого, модернізованого (симпатичного) пожирача голосних! 
user_word = input("Введіть слово: ") # Запропонувати користувачу ввести слово та присвоїти його змінній user_word.
user_word = user_word.upper()

vowels = ['A', 'E', 'I', 'O', 'U']
word_without_vowels = ''

for letter in user_word:
    if letter in vowels:
        continue 
    word_without_vowels += letter

print("Слово без голосних:", word_without_vowels)
