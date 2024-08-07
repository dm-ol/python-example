# Іноді, вибираючи між декількома варіантами коду, доводиться відштовхуватись від його швидкості.
# Ось приклад обчислення часу виконання коду:

import time

# за допомогою модуля time запам'ятовуємо початковий час, виконуємо основний код, дізнаємося про кінцевий час і просто вираховуємо різницю.
time_start = time.perf_counter()

# ВСТАВТЕ ВАШ КОД

time_end = time.perf_counter()
total_time = time_end - time_start

print(f'{total_time:0.2f} seconds have passed')
