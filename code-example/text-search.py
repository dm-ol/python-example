# Для виконання текстових операцій без урахування регістру можна використовувати модуль re та вказати прапор re.IGNORECASE для різних операцій.
# Заміна тексту не буде відповідати регістру тексту. Для виправлення цього скористаємося допоміжною функцією
# matchcase — вона робить заміну залежно від того, які символи використовуються в тексті.

import re
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
