# Метод discard() видаляє елемент із множини тільки тоді, коли елемент присутній у множині. Якщо відсутній — виводиться початкова множина.

fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)
# ['cherry', 'apple']

# Цей метод відрізняється від методу remove(), який викликає помилку, якщо вказаний елемент не існує (натомість discard() не викликає помилки).
