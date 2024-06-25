# Найчастіше обробка вхідних даних в Python зводиться до перетворення символів у верхній чи нижній регістр.
# Іноді дані можна очистити за допомогою регулярного виразу. Коли завдання ускладняється,
# можна застосувати зручніший спосіб: за допомогою словника зі значеннями для
# заміни символів та методу translate отримаємо лаконічний код.

raw_text = 'This\nstring has\tsome whitespaces\r\n'

character_map = {
    ord('\n'): ' ',
    ord('\t'): ' ',
    ord('\r'): None
}

text = raw_text.translate(character_map)

print(text)  # 'This string has some whitespaces '
