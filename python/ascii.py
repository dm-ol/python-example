# Функція ascii() замінює недрукований символ його відповідним ASCII-значенням та повертає його.

text1 = '√ represents square root'

# Замінюємо √ на ASCII-значення
print(ascii(text1))

text2 = 'Thör is coming'

# Замінюємо ö на ASCII-значення
print(ascii(text2))

# Функція ascii() зі списком
list = ['Python', 'öñ', 5]

print(ascii(list))

# Функція ascii() з множиною

set = {'Π', 'Φ', 'η'}

print(ascii(set))

#
