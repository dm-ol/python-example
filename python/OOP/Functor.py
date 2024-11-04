# Функтори

# Функціональні об'єкти (функтори) є дуже корисними — вони значно гнучкіші,
# ніж функції, оскільки можуть містити додаткові атрибути та методи,
# успадковуватись від інших класів і мати спадкоємців.

class Functor(object):
    def __init__(self, n=10):
        self.n = n

    def __call__(self, x):
        x_first = x[0]
        if type(x_first) is int:
            return self. __MergeSort(x)
        if type(x_first) is float:
            return self. __HeapSort(x)
        else:
            return self. __QuickSort(x)
# Особливо важливим є те, що функтори можуть виступати в ролі декораторів,
# доповнюючи функціональність функцій і класів.
