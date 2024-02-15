# Ваше завдання ‒ написати і протестувати функцію, яка приймає два аргументи (рік і місяць)
# і повертає кількість календарних днів в місяці для заданої пари рік-місяць.
# Ми рекомендуємо вам використовувати список, заповнений значеннями тривалості місяців.
# Можна створити його всередині функції ‒ цей трюк значно скоротить код.
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    # Створення списку тривалості місяців, 28 днів для лютого буде змінено у випадку високосного року
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Якщо рік високосний, змінюємо тривалість лютого
    if is_year_leap(year) and month == 2:
        return 29
    else:
        return month_lengths[month - 1]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Помилка")
