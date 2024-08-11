# За допомогою модуля re можна перевірити допустимі символи.
# У цьому прикладі ми дозволяємо використання великих і маленьких літер англійської мови, а також цифр.
# При потребі можна адаптувати дозволені символи. Наприклад, вираз [^a-z0-9.] вказує на заборону великих літер.

import re


def is_allowed(string):
    characherRegex = re.compile(r'[^a-zA-Z0-9.]')
    string = characherRegex.search(string)
    return not bool(string)


print(is_allowed("abyzABYZ0099"))
# True
print(is_allowed("#*@#$%^"))
# False


# Для виконання текстових операцій без урахування регістру можна використовувати модуль re та вказати прапор re.IGNORECASE для різних операцій.

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
# UPPER snake, lower snake, Mixed snake


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
# UPPER SNAKE, lower snake Mixed Snake
