# Скрипт для автоматичного надсилання електронної пошти

import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

# Установки електронної пошти

smtp_server = 'smtp.example.com'

smtp_port = 587

sender_email = 'Ваша адреса електронної пошти'

receiver_email = 'адреса одержувача'

password = 'ваш_пароль'

# Створення повідомлення

message = MIMEMultipart()

message['From'] = sender_email

message['To'] = receiver_email

message['Subject'] = 'Тема листа'

body = 'Текст повідомлення'

message.attach(MIMEText(body, 'plain'))

# Відправка повідомлення

with smtplib.SMTP(smtp_server, smtp_port) as server:

    server.starttls()

    server.login(sender_email, password)

    server.send_message(message)
