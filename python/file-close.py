# Коли ми перестали виконувати операції з файлом, нам потрібно його правильно закрити.
# Закриття файлу звільняє ресурси, які були використані для роботи з ним.
# Це робиться за допомогою методу close()

# Відкриваємо файл
file1 = open("sample.txt", "r")

# Читаємо файл
read_content = file1.read()
print(read_content)

# Закриваємо файл
file1.close()


# В Python ми можемо використовувати синтаксис with...open для автоматичного закриття файлу.

with open("sample.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)
