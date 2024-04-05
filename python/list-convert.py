# Функція list() повертає список в Python. Наприклад:

text = 'Python'

# Конвертуємо рядок у список
text_list = list(text)
print(text_list)

# Перевіряємо тип text_list
print(type(text_list))

# Порожній список
print(list())

# Рядок голосних
vowel_string = 'aeiou'
print(list(vowel_string))

# Кортеж голосних
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))

# Список голосних
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(list(vowel_list))

# Множина голосних
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(list(vowel_set))

# Словник голосних
vowel_dictionary = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
print(list(vowel_dictionary))

# Об'єкти цього класу є ітераторами


class PowTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if (self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result


pow_two = PowTwo(5)
pow_two_iter = iter(pow_two)

print(list(pow_two_iter))
