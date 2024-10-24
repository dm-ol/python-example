# Модуль bisect забезпечує підтримку вставки значень у відсортований список без необхідності сортувати цей список після кожної вставки.

# Для довгих списків елементів з дорогими операціями порівняння це може бути краще порівняно з більш поширеним підходом.
import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDBA'):
    i = bisect(breakpoints, score)
    return grades[i]


[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
# ['F', 'A', 'C', 'C', 'B', 'A', 'A']

# Модуль називається bisect, тому що він використовує базовий алгоритм розподілу навпіл для виконання своєї роботи.
