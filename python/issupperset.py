# Метод issuperset() повертає True, якщо множина містить усі елементи іншої множини (передається як аргумент). Якщо ні, то повертається False.

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)  # True

# Також можна використовувати оператор >=, проте він вимагає множин по обидва боки. Метод issuperset може приймати будь-який об'єкт.
