# Мало кому сподобається перспектива ручної реалізації операторів порівняння для якого-небудь класу.
# Чи можна спростити це нудне завдання? Так, можна — за допомогою декоратора functools.total_ordering.

from functools import total_ordering


@total_ordering
class Number:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


print(Number(20) > Number(3))
print(Number(1) < Number(5))
print(Number(15) >= Number(15))
print(Number(10) <= Number(2))
