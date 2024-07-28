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


# Як функція len() працює зі словниками та множинами?

testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))

# Порожня множина
testSet = set()
print(testSet, 'length is', len(testSet))

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

testDict = {}
print(testDict, 'length is', len(testDict))

testSet = {1, 2}
# Заморожена множина
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))


# Як працює функція len() з об’єктами користувача?

class Session:
    def __init__(self, number=0):
        self.number = number

    def __len__(self):
        return self.number


# Довжина за замовчуванням дорівнює 0
s1 = Session()
print(len(s1))

# Вказуємо довільну довжину
s2 = Session(6)
print(len(s2))
