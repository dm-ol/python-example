# Метод zfill() повертає копію рядка із символами '0', доповненими ліворуч.
# Параметр width визначає довжину рядка, що повертається функцією zfill().

text = "program is fun"
print(text.zfill(15))  # program is fun
print(text.zfill(20))  # 000000program is fun
print(text.zfill(10))  # program is fun

number = "-290"
print(number.zfill(8))  # -0000290
number = "+290"
print(number.zfill(8))  # +0000290
text = "--random+text"
print(text.zfill(20))  # -0000000-random+text

# Припустимо, що початкова довжина рядка дорівнює 10, а width — 15.
# Тоді zfill() повертає копію рядка з п'ятьма цифрами '0', заповненими зліва.
# Якщо параметр width менший за довжину рядка, повертається вихідний рядок.
