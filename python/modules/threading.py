# У модулі threading новий потік виконання може починатися з нового threading.Thread та присвоєння йому функції для виконання.

import threading


def foo():
    print("Hello threading!")


my_thread = threading.Thread(target=foo)

print(type(my_thread))


my_thread.start()


# Параметр target посилається на функцію (або об'єкт, що викликається), яка буде працювати.
#                                         Нитка не почне виконання до start, також не викликатиметься Thread об'єкта.

# Коли my_thread завершується, виклик start викине виняток RuntimeError.
# Якщо хочете запустити Thread у фоновому режимі, передавайте daemon=True або встановіть my_thread.daemon в True перед викликом start().
