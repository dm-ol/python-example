# Функція callable() повертає True, якщо вказаний об’єкт викликається, в протилежному випадку повертається False.
# Важливо пам’ятати, що навіть якщо callable() повертає True, виклик об’єкта може призвести до помилки.
# Проте, якщо callable() повертає False, виклик об’єкта неодмінно призведе до помилки.

# Як працює функція callable()?

x = 5
print(callable(x))


def testFunction():
    print("Test")


y = testFunction
print(callable(y))
