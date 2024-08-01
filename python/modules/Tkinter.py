# Python Tkinter – це стандартна бібліотека Python для створення графічного користувацького інтерфейсу.

# Основні компоненти та віджети Tkinter містять у собі:

# Вікно (Window) – основний контейнер, у якому розміщуються всі віджети та елементи інтерфейсу.
# Кнопка (Button) – елемент керування, який реагує на натискання користувача.
# Мітка (Label) – елемент для відображення тексту або зображення на інтерфейсі.
# Текстове поле (Entry) – віджет для введення тексту користувачем.
# Фрейм (Frame) – контейнер, який групує та керує розташуванням інших компонентів.

# Базові налаштування


import Tkinter as tk

# Створення головного вікна

root = tk.Tk()

root.title("Приклад Tkinter")

# Додавання мітки

label = tk.Label(root, text="Привіт, Tkinter!")

label.pack()

# Додавання кнопки

button = tk.Button(root, text="Натисни мене")

button.pack()

# Запуск головного циклу обробки подій

root.mainloop()


# Керування поведінкою віджетів


def button_click():

    label.config(text="Кнопка натиснута!")


root = tk.Tk()

label = tk.Label(root, text="Привіт, користувачу!")

button = tk.Button(root, text="Натисни мене", command=button_click)

label.pack()

button.pack()

root.mainloop()


# Розробка інтерактивних форм

def submit_form():

    user_input = entry.get()

    result_label.config(text=f"Привіт, {user_input}!")


root = tk.Tk()

entry = tk.Entry(root)

submit_button = tk.Button(root, text="Відправити", command=submit_form)

result_label = tk.Label(root, text="Введіть ваше ім'я:")

entry.pack()

submit_button.pack()

result_label.pack()

root.mainloop()
