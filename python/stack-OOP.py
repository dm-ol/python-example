# Стек - об'єктний підхід

class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        print("Hi!")


stack_object = Stack()  # Instantiating the object.


class Stack:
    def __init__(self):
        self.stack_list = []


stack_object = Stack()
print(len(stack_object.stack_list))

# Якщо будь-який компонент класу має назву, що починається з двох підкреслень (__),
# він стає приватним – це означає, що до нього можна отримати доступ лише з класу.
# Incapsulation


class Stack:
    def __init__(self):
        self.__stack_list = []


stack_object = Stack()
print(len(stack_object.__stack_list))
