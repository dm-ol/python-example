# Сортування — витратний процес. Якщо ви маєте відсортовану послідовність, краще залишити її такою.
# В Python для цього можна використати функцію bisect.insort. insort(seq, item) вставляє item у seq,
# щоб зберегти послідовність у порядку зростання — приймає необов'язкові аргументи lo, hi, щоб обмежити пошук підпослідовністю.

import bisect
import random
SIZE = 7
random.seed(1729)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('- ->' % new_item, my_list)
