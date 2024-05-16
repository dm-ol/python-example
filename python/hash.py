# Функція hash() повертає хеш-значення об’єкта, якщо воно в нього є.
# Хеш-значення — це просто цілі числа, які використовуються для
# порівняння ключів словника під час його швидкого перегляду.
# Синтаксис функції hash(): hash(object)

text = 'Python Programming'

# Обчислюємо хеш-значення змінної text
hash_value = hash(text)
print(hash_value)

# Хеш для цілого числа не змінюється
print('Hash for 181 is:', hash(181))

# Хеш для десяткового числа
print('Hash for 181.23 is:', hash(181.23))

# Хеш для рядка
print('Hash for Python is:', hash('Python'))

# Кортеж голосних
vowels = ('a', 'e', 'i', 'o', 'u')

print('The hash is:', hash(vowels))

# Функція hash() для об’єктів користувача шляхом перевизначення методу __hash__()


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))


person = Person(23, 'Adam')
print(hash(person))
