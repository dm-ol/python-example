# add() додає заданий елемент у множину. Якщо елемент вже присутній,
# метод не додає жодного елемента. Також можна додати кортежі до множини.
# Як і у випадку зі звичайними елементами, той самий кортеж можна додати лише один раз.
vowels = {'a', 'e', 'i', 'u'}

vowels.add('o')
print('Vowels are:', vowels)

# Vowels are: {'a', 'i', 'o', 'u', 'e'}

vowels.add('a')
print('Vowels are:', vowels)
# Vowels are: {'a', 'i', 'o', 'u', 'e'}
