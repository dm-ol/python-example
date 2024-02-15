# Ваше завдання полягає в тому, щоб написати та перевірити функцію,
# яка приймає три аргументи (рік, місяць і день місяця) і повертає
# відповідний день року або повертає None, якщо будь-який з аргументів є некоректним.
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


def day_of_year(year, month, day):
    # Перевірка на коректність введених значень
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    # Загальна кількість днів у попередніх місяцях
    total_days = sum(days_in_month(year, m) for m in range(1, month))

    # Додавання днів поточного місяця
    total_days += day

    return total_days


print("Номер дня:", day_of_year(2000, 5, 31))
