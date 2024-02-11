# Зміна та додавання значень. Оскільки словники є повністю
# змінюваними, немає жодних перешкод для їхньої модифікації.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary['cat'] = 'minou' # замінимо значення "chat" на "minou"
print(dictionary)

# Додавання нового ключа
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary['swan'] = 'cygne' # новий ключ
print(dictionary)
 
# or
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary.update({"duck": "canard"}) # новий ключ
print(dictionary)

# Видалення ключа
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
del dictionary['dog']
print(dictionary)
 

 
