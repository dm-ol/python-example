# Модуль inspect стане в нагоді для розуміння того, що відбувається за лаштунками в Python.
# Ви навіть можете викликати його методи на них же! Метод inspect.getsource() виводить власний вихідний код,
# а inspect.getmodule() — модуль, в якому його визначили. Остання команда виводить номер рядка, де й знаходиться.

import inspect

print(inspect.getsource(inspect.getsource))
print(inspect.getmodule(inspect.getmodule))
print(inspect.currentframe().f_lineno)
