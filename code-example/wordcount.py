# Отримати ім’я файлу та відкрити його
name = input('Вкажіть шлях до файлу:') 
handle = open(name, 'r')

# Рахувати частоту слів
counts = dict()
for line in handle: 
    words = line.split() 
    for word in words:
        counts[word] = counts.get(word,0) + 1

# Знайти найуживаніше слово
bigcount = None 
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount: 
        bigword = word
        bigcount = count

# Готово
print("Найвживаніше слово:", bigword)
print("Кількість раз:", bigcount)
