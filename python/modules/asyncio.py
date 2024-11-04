# Асинхронний код.
# На відміну від синхронного коду, який виконує кожну задачу послідовно,
# асинхронний код може запустити кілька завдань "паралельно" та організувати
# їх виконання за допомогою ітерацій та викликів колббеків.

import asyncio


async def hello():
    await asyncio.sleep(1)
    print("Hello")


async def world():
    await asyncio.sleep(2)
    print("World")


async def main():
    await asyncio.gather(hello(), world())

if __name__ = '__main__':
    asyncio.run(main())
