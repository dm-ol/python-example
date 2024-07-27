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


# Викликаний об’єкт

class Foo:
    def __call__(self):
        print('Print Something')


print(callable(Foo))


class Foo:
    def __call__(self):
        print('Print Something')


InstanceOfFoo = Foo()

InstanceOfFoo()


# Об’єкт може викликатися, але не викликається

class Foo:
    def printLine(self):
        print('Print Something')


print(callable(Foo))


# Об’єкт класу Foo може викликатися, але не викликається. Наступний код спричинить помилку:

class Foo:
    def printLine(self):
        print('Print Something')


print(callable(Foo))

InstanceOfFoo = Foo()

# Тут помилка
InstanceOfFoo()
