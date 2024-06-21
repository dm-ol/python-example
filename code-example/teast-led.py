# You've surely seen a seven-segment display.

# It's a device (sometimes electronic, sometimes mechanical) designed to present
# one decimal digit using a subset of seven segments.
# If you still don't know what it is, refer to the following Wikipedia article.

# Your task is to write a program which is able to simulate the work of a seven-display device,
# although you're going to use single LEDs instead of segments.
# Масив бінарних строк, які представляють цифри від 0 до 9
# у вигляді семисегментного індикатора
digits = ['1111110',  	# 0
          '0110000',    # 1
          '1101101',    # 2
          '1111001',    # 3
          '0110011',    # 4
          '1011011',    # 5
          '1011111',    # 6
          '1110000',    # 7
          '1111111',    # 8
          '1111011',    # 9
          ]

# Функція для виводу числа у вигляді семисегментного індикатора


def print_number(num):
    global digits  # Використовуємо глобальну змінну digits
    digs = str(num)  # Перетворюємо число на строку
    # Ініціалізуємо пусті строки для кожного рядка
    lines = ['' for lin in range(5)]
    for d in digs:
        # Створюємо порожні сегменти для цифри
        segs = [[' ', ' ', ' '] for lin in range(5)]
        ptrn = digits[ord(d) - ord('0')]  # Отримуємо шаблон для даної цифри
        if ptrn[0] == '1':  # Верхня горизонтальна лінія
            segs[0][0] = segs[0][1] = segs[0][2] = '#'
        if ptrn[1] == '1':  # Права верхня вертикальна лінія
            segs[0][2] = segs[1][2] = segs[2][2] = '#'
        if ptrn[2] == '1':  # Права нижня вертикальна лінія
            segs[2][2] = segs[3][2] = segs[4][2] = '#'
        if ptrn[3] == '1':  # Нижня горизонтальна лінія
            segs[4][0] = segs[4][1] = segs[4][2] = '#'
        if ptrn[4] == '1':  # Ліва нижня вертикальна лінія
            segs[2][0] = segs[3][0] = segs[4][0] = '#'
        if ptrn[5] == '1':  # Ліва верхня вертикальна лінія
            segs[0][0] = segs[1][0] = segs[2][0] = '#'
        if ptrn[6] == '1':  # Середня горизонтальна лінія
            segs[2][0] = segs[2][1] = segs[2][2] = '#'
        for lin in range(5):
            # Додаємо сегменти до відповідних рядків
            lines[lin] += ''.join(segs[lin]) + ' '
    for lin in lines:
        print(lin)  # Виводимо кожен рядок


# Запитуємо у користувача число та виводимо його у вигляді семисегментного індикатора
print_number(int(input("Enter the number you wish to display: ")))
