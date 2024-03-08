# Пакет pytesseract, який дозволяє парсити текст з картинок
# за допомогою оптичного розпізнавання символів. Щоб отримати
# текст з картинки, викликаємо метод image_to_string.
# Якщо текст англійською, вкажіть аргумент lang як 'eng'.
# Для відкриття картинок можна використовувати pillow,
# або просто вказати шлях до файлу у вигляді рядка.

from PIL import Image
import pytesseract

# Конвертуємо картинку в текст та виводимо результат
print(pytesseract.image_to_string(Image.open('test.png')))

# Вказуємо англійську мову в аргументах
print(pytesseract.image_to_string('test-english.jpg', lang='eng'))

try:
    # Задаємо максимальний час очікування
    print(pytesseract.image_to_string('test.jpg', timeout=2))
except RuntimeError as timeout_error:
    pass
