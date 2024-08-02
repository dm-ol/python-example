# Стандартна бібліотека Python 3 містить модуль pathlib (https://docs.python.org/3/library/pathlib.html),
# що включає функцію Path(), достатню для повноцінної роботи з файловими шляхами.
# Однією з найкрутіших фіч у роботі із шляхами є заміна os.path.join() на зручніший і елегантніший варіант.
# По суті ця бібліотека замінює функції, що використовуються для роботи із шляхами,
# з модуля os (наприклад, os.mkdir або os.path) на більш зручні.

from pathlib import Path
usr = Path('/usr')
config = usr / '.config' / 'pep8'
str(config)
'/usr/.config/pep8'
config.name
'pep8'


p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
p.with_suffix('.bz2')

p = PureWindowsPath('README')
p.with_suffix('.txt')

p = PureWindowsPath('README.txt')
p.with_suffix('')
