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
