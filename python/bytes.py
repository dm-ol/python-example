# Функція bytes() повертає незмінюваний об’єкт bytes, ініціалізований вказаними даними та розміром.

message = 'Python is fun'

# Конвертуємо рядок у байти
byte_message = bytes(message, 'utf-8')
print(byte_message)
