# Пакет Pillow дозволяє додавати водяні знаки на зображення.
# Для цього вам знадобляться модулі Image, ImageDraw та ImageFont із пакета Pillow.

# Модуль ImageDraw додає функціональність для малювання 2D-графіки на нових або наявних зображеннях,
# а ImageFont використовується для завантаження файлів растрових зображень, шрифтів TrueType та OpenType.

from PIL import Image, ImageDraw, ImageFont
# Створюємо обʼєкт
im = Image.open('image.jpg')
width, height = im.size
draw = ImageDraw.Draw(im)
text = "sample watermark"
font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)
# Рахуємо координати тексту
margin = 10
x = width - textwidth - margin
y = height - textheight - margin
# Малюємо водяний знак у правому нижньому кутку
draw.text((x, y), text, font=font)
im.show()
# Зберігаємо нове зображення
im.save('watermark.jpg')
