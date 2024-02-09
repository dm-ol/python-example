import random
import heapq

x = [random.randint(0, 200) for _ in range(100)]

print (heapq.nsmallest (5, x))
print (heapq.nlargest(5, x))

