# В Python лямбда-функція (або “анонімна функція”) — це спеціальний тип функції без імені.
# Ключове слово lambda (замість def) використовується для створення лямбда-функції. lambda аргумент(и) : вираз

# Оголошуємо лямбда-функцію
# greet = lambda : print('Hello, World!')
def greet(): return print('Hello, World!')


# Викликаємо лямбда-функцію
greet()


# Лямбда-функція, яка приймає 1 аргумент
# greet_user = lambda name : print('Hey there,', name)
def greet_user(name): return print('Hey there,', name)


# Виклик лямбда-функції
greet_user('Delilah')
