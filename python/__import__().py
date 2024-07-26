# При написанні коду може виникнути необхідність використання якихось конкретних модулів.
# Імпортувати модуль можна за допомогою одного рядка коду в Python. Але як бути,
# якщо ім’я потрібного модуля стане відомим лише під час виконання?
# Як ми можемо імпортувати такий модуль? Ми можемо використати вбудовану функцію __import__(),
# яка допомагає імпортувати модулі під час виконання коду.

# Функція __import__() приймає 5 параметрів:
#    name — ім’я модуля, який ми хочемо імпортувати;
#    globals та locals — визначають, як інтерпретувати name;
#    fromlist — назви об’єктів чи підмодулів, які потрібно імпортувати за ім’ям;
#    level — вказуємо, використовувати абсолютний чи відносний імпорт.

# __import__(name, globals=None, locals=None, fromlist=(), level=0)

# Як працює функція __import__()?

mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5))