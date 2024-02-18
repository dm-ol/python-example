def subgen(n):  # підгенератор
    for i in range(n):
        yield i


def delegator(source):  # делегуючий генератор
    # for item in source:
    #     yield item
    yield from source


g = subgen(5)

for j in delegator(g):
    print(j, end=' ')

# Output: 0 1 2 3 4
