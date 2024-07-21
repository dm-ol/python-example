# Функція staticmethod() повертає статичний метод для цієї функції.
# Коли слід використовувати статичні методи?
# 1. Допоміжна функція для класу
# Статичні методи мають обмежений варіант використання, оскільки, як і методи класу або будь-які інші методи всередині класу, вони не можуть отримати доступ до властивостей самого класу.

# Однак, коли потрібна допоміжна функція, яка не звертається до жодних властивостей класу, але потрібна її приналежність до класу, слід використовувати статичні методи.

class Calculator:

    def add_numbers(num1, num2):
        return num1 + num2


# Конвертуємо метод add_numbers() у статичний метод
Calculator.add_numbers = staticmethod(Calculator.add_numbers)

sum = Calculator.add_numbers(5, 7)
print('Sum:', sum)

# Статичні методи, як і методи класу — це методи, які прив’язані до класу,
# а не до його об’єкта. Вони не потребують створення об’єкта класу. Таким чином вони не залежать від стану об’єкта.
# Різниця між статичним методом та методом класу полягає в наступному:
#    статичні методи нічого не знають про клас і працюють лише з параметрами;
#    метод класу працює із класом, оскільки його параметром завжди є сам клас.
# Вони можуть бути спричинені як самим класом, так і його об’єктом:
#   Class.staticmethodFunc()
#   Class().staticmethodFunc()

# Створення статичного методу за допомогою функції staticmethod()


class Mathematics:

    def addNumbers(x, y):
        return x + y


# Створюємо статичний метод addNumbers()
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))


# Створення допоміжної функції в якості статичного методу

class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if (date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")
