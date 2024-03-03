# Корисний пакет spellchecker дозволяє знаходити друкарські
# помилки і навіть дає можливі варіанти виправлень.
# Під капотом — алгоритм відстані Левенштейна. А сам код заснований на статті,
# (https://norvig.com/spell-correct.html) написаній у блозі Пітера Норвіга.

from spellchecker import SpellChecker

spell = SpellChecker()

# Знаходимо слова, написані неправильно
misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

# Проходимося по словах з помилками
for word in misspelled:
    # Неправильно написане слово: 'happenning'
    print(spell.correction(word))

    # Можливі виправлення: {'happenning', 'hapening'}
    print(spell.candidates(word))
