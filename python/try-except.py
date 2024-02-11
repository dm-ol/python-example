# Використання виразів try\except
rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0 :
    print('Nice work')
else:
    print('Not a number')
 
# Два винятки після одного try
try:
    value = int(input('Введіть натуральне число: '))
    print('Обернене число для', value, 'дорівнює', 1/value) 
except ValueError:
    print('Помилка. Введене некоректне число') 
except ZeroDivisionError:
    print('Ділення на нуль не допускається.') 
    
# Виняток за замовчуванням. Гілка except за замовчуванням повинна бути останньою гілкою except. Завжди!
try:
    value = int(input('Введіть натуральне число: '))
    print('Обернене число для', value, 'дорівнює', 1/value) 
except ValueError:
    print('Помилка. Введене некоректне число') 
except ZeroDivisionError:
    print('Ділення на нуль не допускається.') 
except:
  print('Тут сталося щось дивне... Вибачте!')