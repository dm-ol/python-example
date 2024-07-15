# Коли знадобиться визначити з отриманого рядка літеральний тип
# (рядки, числа, списки, кортежі, словники, логічні значення та None),
# можемо скористатися функцією literal_eval() із модуля ast.

from ast import literal_eval

example = literal_eval("{'a': 1, 'b': 2}")
type(example)

print(example)
{'a': 1, 'b': 2}
