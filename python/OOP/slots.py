# Якщо ви писали програми, які створюють велику кількість екземплярів якогось класу,
# то могли помітити, що їм несподівано може знадобитися дуже багато пам'яті.
# Це відбувається через те, що Python використовує словники для представлення атрибутів екземплярів класів.

class Person:
    __slots__ = ["first_name", "last_name", "phone"]


def init__(self, first_name, last_name, phone):
    self. first_name = first_name
    self. last_name = last_name
    self. phone = phone
