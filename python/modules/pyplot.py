# Із pyplot можна використовувати функцію pie() для малювання кругових діаграм.
# Кругова діаграма малює одну частину (клин) кожного значення в масиві.

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylabels)
plt.show()

# За замовчуванням побудова першого клину починається з осі X праворуч і рухається проти годинникової стрілки.
