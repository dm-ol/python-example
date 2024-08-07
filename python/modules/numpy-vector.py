# Одним із прийомів для прискорення роботи циклів є векторизація обчислень,
# тобто використання функцій, що підтримують операції над векторами.

import numpy as np


def my_func(a, b):
    if a > b:
        return a - b
    else:
        return a + b


vfunc = np.vectorize(my_func)
vfunc([1, 2, 3, 4], 2)
array([3, 4, 1, 2])

# У прикладі вище для роботи з функцією my_func ми могли б викликати її в циклі кожного елемента списку,
# але набагато простіше використовувати vectorize. По суті, vectorize перетворює функцію так,
# що вона починає приймати весь вектор цілком, а не окремий його елемент. Щоправда, іноді прискорення є незначним.


def mypolyval(p, x):
    _p = list(p)
    res = _p.pop(0)
    while _p:
        res = res*x + _p.pop(0)
    return res


vpolyval = np.vectorize(mypolyval, excluded=['p'])
vpolyval(p=[1, 2, 3], x=[0, 1])
array([3, 6])
