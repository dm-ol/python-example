# При зберіганні HTML у базах даних чи змінних вам потрібно екранувати спеціальні символи,
# які є текстом розмітки, але можуть бути переплутані як такі. До таких символів належать <, >, ", ' та &.
# Якщо не використовувати екранування, браузер неправильно відобразить веб-сторінку.
# Щоб уникнути цих символів, ми можемо використовувати метод html.escape(). Він кодує HTML у рядок ascii.

import html
s = 'Elements are written as "<tag>text</tag>".'
print(s)
# Elements are written as "<tag>text</tag>".
print(html.escape(s))
# Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.

# Відключаємо екранування лапок
print(html.escape(s, quote=False))
# Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".
