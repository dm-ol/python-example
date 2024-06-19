# Модуль textwrap дозволяє скоротити текст до певної кількості символів без переривання на середині слова.

# Слова переносяться на нові рядки й нічого не обривається на півслові.
import textwrap

text = """The textwrap module can be used to format text for output in
situations where pretty-printing is desired."""

textwrap.fill(text, width=20)
