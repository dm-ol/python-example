# Коли модуль імпортується, його вміст неявно виконується Python
import sys
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

# Path to modules
for p in sys.path:
    print(p)
