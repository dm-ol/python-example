# Модуль textwrap дозволяє скоротити текст до певної кількості символів без переривання на середині слова.
# https://docs.python.org/uk/3/library/textwrap.html

# Слова переносяться на нові рядки й нічого не обривається на півслові.
import textwrap

text = """The textwrap module can be used to format text for output in
situations where pretty-printing is desired."""

textwrap.fill(text, width=20)


# Скорочення тексту. Першим аргументом передається рядок, другим вказуємо кількість символів,
# що має містити результат. Також третім аргументом можна передати заготівлю,
# яка вставлятиметься наприкінці обрізаного рядка.
textwrap.shorten(text, 40, placeholder='... ')
