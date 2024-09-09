# Використання collections.Counter для підрахунку частоти елементів у колекції

# Коли вам потрібно підрахувати, як часто трапляється кожен елемент у списку або іншій колекції,
# Counter з модуля collections надає простий і ефективний спосіб зробити це.

# Використання Counter спрощує процес підрахунку частоти елементів, даючи змогу легко
# і швидко отримати необхідну інформацію і виконати додаткові операції з частотними даними.

from collections import Counter

# Список елементів

items = ['apple', 'banana', 'orange', 'pineapple',
         'apple', 'banana', 'qiwi', 'banana']

# Підрахунок елементів

item_count = Counter(items)

print(item_count)

# Підрахунок конкретного елемента

print("Banana:", item_count['banana'])
print("Apple:", item_count['apple'])
