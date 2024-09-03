# Деструктори викликаються при знищенні об’єкта. В Python деструктори не є обов’язковими, як у C++, тому що Python має збирач сміття, який автоматично виконує керування пам’яттю.
# Метод __del__() відомий як функція-деструктор у Python. Він викликається, коли всі посилання на об’єкт були видалені, тобто коли об’єкт очищується збирачем сміття.
# Синтаксис оголошення деструктора в Python:

# def __del__(self):
#       тіло деструктора

# Примітка: Посилання на об’єкт також видаляється, коли об’єкт виходить з області видимості або коли програма завершує своє виконання.
# Розглянемо приклад використання деструктора в Python:

class Employee:
    # Конструктор класу
    def __init__(self):
        print('Employee created.')

    # Деструктор класу
    def __del__(self):
        print('Destructor called, Employee deleted.')


obj = Employee()
del obj
# Результат:

# Employee created.
# Destructor called, Employee deleted.
# Використовуючи ключове слово del, ми видалили всі посилання на об’єкт obj, тому деструктор був викликаний автоматично.
# Примітка: Деструктор викликається після завершення програми або коли всі посилання на об’єкт видалені, тобто коли лічильник посилань стає рівним нулю, а не коли об’єкт виходить з області видимості.


# Наступний приклад дає пояснення до вищезгаданої примітки. Зверніть увагу, що деструктор викликається після виводу рядка Program End...:

class Employee:
    # Конструктор класу
    def __init__(self):
        print('Employee created')

    # Деструктор класу
    def __del__(self):
        print("Destructor called")


def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj


print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

# Результат:

# Calling Create_obj() function...
# Making Object...
# Employee created
# function end...
# Program End...
# Destructor called
