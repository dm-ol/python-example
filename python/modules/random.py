import random
import heapq

x = [random.randint(0, 200) for _ in range(100)]

print(heapq.nsmallest(5, x))
print(heapq.nlargest(5, x))


# betavariate() — видає випадкове число з плаваючою комою від 0 до 1 на основі бета-розподілу (для статистичних розрахунків).

random.betavariate(alpha=2, beta=5)

# gauss() — генерує випадкове число з плаваючою комою на основі розподілу Гаусса (використовується в теорії ймовірності).

random.gauss(mu=5, sigma=3)

# paretovariate() — повертає випадкове число з плаваючою комою на основі розподілу Парето (використовується в теорії ймовірності).

random.paretovariate(alpha=10)
