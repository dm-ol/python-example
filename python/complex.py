# Функція complex() повертає комплексне число, вказуючи дійсну та уявну частини.
# Функція complex() приймає два параметри:
#   real — дійсна частина. Якщо параметр real пропущено, то значенням за замовчуванням є 0.
#   imag — уявна частина. Якщо параметр imag пропущено, то значенням за замовчуванням є 0.
# Якщо перший параметр, який передається в функцію, є рядком, то його буде інтерпретовано
# як комплексне число. В такому випадку другий параметр передавати не потрібно.

# complex([real[, imag]])

# Як випливає з назви, функція complex() повертає комплексне число. Якщо рядок,
# переданий у функцію, є недопустимим комплексним числом, виникне помилка ValueError.

z = complex(2, -3)
print(z)

z = complex(1)
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)

# Комплексне число можна створити без використання функції complex().
# Для цього потрібно вказати 'j' або 'J' після числа.

a = 2+3j
print('a =', a)
print('Type of a is', type(a))

b = -2j
print('b =', b)
print('Type of b is', type(a))

c = 0j
print('c =', c)
print('Type of c is', type(c))

# Математичні операції з комплексними числами

comp_a = 10 + 12j
comp_b = 4 + 5j

print(comp_a + comp_b)
print(comp_a - comp_b)
print(comp_a * comp_b)
print(comp_a / comp_b)
