# Стандартна бібліотека Python 3 містить модуль pathlib (https://docs.python.org/3/library/pathlib.html),
# що включає функцію Path(), достатню для повноцінної роботи з файловими шляхами.
# Однією з найкрутіших фіч у роботі із шляхами є заміна os.path.join() на зручніший і елегантніший варіант.

from pathlib import Path
usr = Path('/usr')
config = usr / '.config' / 'pep8'
str(config)
'/usr/.config/pep8'
config.name
'pep8'
