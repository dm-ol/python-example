# Щоб видалити файл, імпортуємо модуль os, перевіряємо існування файлу і застосовуємо функцію os.remove().

import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

import os
os.rmdir("myfolder")

# Якщо треба видалити всю папку, використовуємо метод os.rmdir().
