# Пакет schedule дозволяє планувати завдання та повторювати їх через проміжок часу.
# Він є максимально інтуїтивним і має гнучкий функціонал.
# А ще — schedule не вимагає зовнішніх залежностей і сам є загалом легким.

import python.modules.schedule as schedule


def job():
    print("I'm working...")


schedule.every(1).seconds.do(job)  # Кожну секунду
schedule.every().hour.do(job)  # Кожну годину
schedule.every().day.at("10:30").do(job)  # Кожен день о 10:30
schedule.every().monday.do(job)  # Кожен понеділок
schedule.every().wednesday.at("13:15").do(job)  # Кожну середу о 13:15

while True:
    schedule.run_pending()
