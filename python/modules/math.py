# Модуль math є стандартним модулем в Python і завжди доступний.
# Щоб використовувати математичні функції цього модуля, необхідно
# імпортувати модуль за допомогою стейтменту import math.

import math

x = 5
y = 3

# Повертає найменше ціле число, більше чи рівне x.
math.ceil(x)

# Повертає x зі знаком y.
math.copysign(x, y)

# Повертає абсолютне значення x.
math.fabs(x)

# Повертає факторіал x.
math.factorial(x)

# Повертає найбільше ціле число, менше чи рівне x.
math.floor(x)

# Повертає остачу при діленні x на y.
math.fmod(x, y)

# Повертає мантису та експоненту x у вигляді пари (m, e).
math.frexp(x)

# Повертає точну суму значень типу з плаваючою крапкою в інтегрованому об’єкті.
math.fsum("ітерований_об’єкт")

# Повертає True, якщо x не є ні нескінченністю, ні NaN (Not a Number).
math.isfinite(x)

# Повертає True, якщо x є додатною або від’ємною нескінченністю.
math.isinf(x)

# Повертає True, якщо x є NaN.
math.isnan(x)

# Повертає x * (2**y).
math.ldexp(x, y)

# Повертає дробову та цілу частини x.
math.modf(x)
# Повертає “зрізане” цілочисельне значення x (відкидає дробову частину числа).
math.trunc(x)


math.exp(x)  # Повертає e**x.
math.expm1(x)  # Повертає e**x – 1.
log(x[b])  # Повертає логарифм x за основою b (за замовчуванням e).
math.log1p(x)  # Повертає натуральний логарифм 1+x.
math.log2(x)  # Повертає логарифм x за основою 2.
math.log10(x)  # Повертає логарифм x за основою 10.
pow(x, y)  # Повертає x, піднесений до степеня y.
math.sqrt(x)  # Повертає квадратний корінь з x.
math.acos(x)  # Повертає арккосинус x.
math.asin(x)  # Повертає арксинус x.
math.atan(x)  # Повертає арктангенс x.
math.atan2(y, x)  # Повертає значення atan(y/x) (в радіанах).
math.cos(x)  # Повертає косинус x.
# Обчислює гіпотенузу трикутника з катетами x та y (math.sqrt(x * x + y * y)).
math.hypot(x, y)
math.sin(x)  # Повертає синус x.
math.tan(x)  # Повертає тангенс x.
math.degrees(x)  # Перетворення кута x з радіанів у градуси.
math.radians(x)  # Перетворення кута x з градусів у радіани.
math.acosh(x)  # Повертає зворотний гіперболічний косинус x.
math.asinh(x)  # Повертає зворотний гіперболічний синус x.
math.atanh(x)  # Повертає зворотний гіперболічний тангенс x.
math.cosh(x)  # Повертає гіперболічний косинус x.
math.sinh(x)  # Повертає гіперболічний синус x.
math.tanh(x)  # Повертає гіперболічний тангенс x.
math.erf(x)  # Повертає функцію помилки у точці x.
math.erfc(x)  # Повертає додаткову функцію помилки у точці x.
math.gamma(x)  # Повертає Гамма-функцію у точці x.
# Повертає натуральний логарифм абсолютного значення Гамма-функції у точці x.
math.lgamma(x)
# Математична константа Пі, що дорівнює відношенню довжини кола до його діаметра (3,14159…).
print(math.pi)
# Математична константа e (2,71828…).
print(math.e)