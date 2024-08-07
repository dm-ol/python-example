# Функція format() форматує вказані значення та вставляє їх у заповнювач рядка.
# Заповнювач визначається за допомогою фігурних дужок {}. Функція format() повертає відформатований рядок.
# format(value[, format_spec])
# Функція format() приймає два параметри:
#    value — значення, яке необхідно відформатувати;
#    format_spec — специфікація того, як слід відформатувати значення.

# Специфікатор формату може бути наступним:
# [[fill]align][sign][#][0][width][,][.precision][type]
# де опції:
# fill        ::=  будь-який символ
# align       ::=  "<" | ">" | "=" | "^"
# sign        ::=  "+" | "-" | " "
# width       ::=  ціле число
# precision   ::=  ціле число
# type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

# s - рядок, можна не вказувати, використовується за замовчуванням;
# b - двійковий формат;
# с - перетворює ціле число на символ Unicode;
# d - десятковий формат;
# e - науковий формат, з малою літерою e;
# E - науковий формат, з E верхнім регістром;
# f - формат чисел із плаваючою комою;
# F - формат чисел із плаваючою комою, верхній регістр;
# g - загальний формат, нижній регістр;
# G - загальний формат, верхній регістр;
# o - Восьмирічний формат;
# x - шістнадцятковий формат, нижній регістр;
# X - шістнадцятковий формат, верхній регістр;
# n - формат цілих чисел;
# % - Відсотковий формат. Множить число на 100 і використовує f для виведення. Наприкінці ставиться %

value = 45

# Форматуємо ціле число у двійкове
binary_value = format(value, 'b')
print(binary_value)


# Форматування числа за допомогою функції format()

# d, f та b є скороченнями назв типів даних

# Ціле число
print(format(123, "d"))

# Число з плаваючою крапкою
print(format(123.4567898, "f"))

# Двійкове число
print(format(12, "b"))


# Форматування числа за допомогою fill, align, sign, width, precision та type

# Ціле число
print(format(1234, "*>+7,d"))

# Тут при форматуванні цілого числа 1234 ми вказали специфікатор форматування *>+7,d. Розберемо кожну опцію:
#    * — це символ заповнення, який заповнює порожні місця після форматування;
#    > — це опція вирівнювання по правому краю;
#    + — це опція знаку, яка змушує число мати знак зліва;
#    7 — це опція ширини, яка змушує число приймати мінімальну ширину 7, інші пробіли будуть заповнені символом заповнення;
#    , — це оператор тисяч, який ставить кому між тисячами;
#    d — це тип опції, який вказує, що число є цілим числом.

# Число з плаваючою крапкою
print(format(123.4567, "^-09.3f"))

# При форматуванні числа з плаваючою крапкою 123.4567 ми вказали специфікатор формату ^-09.3f. Розберемо детально:
#    ^ — це опція вирівнювання по центру, яка вирівнює вихідний рядок по центру простору, що залишився;
#    - — це опція знака, яка додає знак від’ємним числам;
#    0 — це символ, який ставиться на місце порожніх місць;
#    9 — це опція ширини, яка встановлює мінімальну ширину числа рівною 9 (включаючи десяткову крапку, кому тисяч і знак);
#    .3 — це оператор точності, який встановлює точність заданого числа з плаваючою крапкою до 3 знаків;
#    f — це опція типу, яка вказує, що число є числом з плаваючою крапкою.


# Використання функції format(), перевизначаючи метод __format__()

# Користувацький метод __format__()
class Person:
    def __format__(self, format):
        if (format == 'age'):
            return '23'
        return 'None'


print(format(Person(), "age"))
