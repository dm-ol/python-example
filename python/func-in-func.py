# Функція може використовувати іншу функцію, як параметр. Приклад:

from datetime import date


def get_weekday():
    return date.today().strftime('%A')

# Функція використовує попередню функцію як параметр за замовчуванням


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()  # Робимо копію initial_post, щоб не змінювати його
    post_copy['created_on_weekday'] = weekday  # Додаємо в post_copy новий ключ
    return post_copy

# Створюєм аргументи для функції


initial_post = {
    'id': 44,
    'author': 'DevDM',
}

# Викликаєм функцію з створеними аргументами

post_with_weekday = create_new_post(initial_post)

print(post_with_weekday)
