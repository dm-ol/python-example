# Змінюємо колір тексту в терміналі

# Наприклад, щоб вивести зелений текст за допомогою Colorama, можна використовувати наведений код.

from colorama import init, Fore
init()
print(Fore.GREEN + 'Цей текст буде зеленим')

# У цьому прикладі init використовується для ініціалізації бібліотеки та забезпечення
# роботи ANSI-послідовностей на Windows, а константа Fore — для встановлення кольору тексту.
