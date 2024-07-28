# Функція len() повертає кількість елементів (довжину) об’єкта.

languages = ['Python', 'Java', 'JavaScript']

# Обчислюємо довжину списку languages
length = len(languages)
print(length)


# Як працює функція len() з кортежами, списками та діапазонами?

testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))


# Як працює функція len() з рядками та байтовими об’єктами?

testString = ''
print('Length of', testString, 'is', len(testString))

testString = 'Python'
print('Length of', testString, 'is', len(testString))

# Байтовий об'єкт
testByte = b'Python'
print('Length of', testByte, 'is', len(testByte))

testList = [1, 2, 3]

# Конвертуємо в байтовий об'єкт
testByte = bytes(testList)
print('Length of', testByte, 'is', len(testByte))
