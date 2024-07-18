# We showed you recently how to extend Stack possibilities by defining a new class (i.e., a subclass)
# which retains all inherited traits and adds some new ones.

# Your task is to extend the Stack class behavior in such a way so that the class is able to count all
# the elements that are pushed and popped (we assume that counting pops is enough). Use the Stack class we've provided in the editor.

# Follow the hints:

# introduce a property designed to count pop operations and name it in a way which guarantees it is hidden;
# initialize it to zero inside the constructor;
# provide a method which returns the value currently assigned to the counter (name it get_counter()).

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1
        return Stack.pop(self)


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())


# As you already know, a stack is a data structure realizing the LIFO (Last In – First Out) model.
# It's easy and you've already grown perfectly accustomed to it.

# Let's try something new now. A queue is a data model characterized by the term FIFO:
# First In – First Out. Note: a regular queue (line) you know from shops or post offices works exactly
# in the same way – a customer who came first is served first too.

# Your task is to implement the Queue class with two basic operations:

# put(element), which puts an element at end of the queue;
# get(), which takes an element from the front of the queue and returns
# it as the result (the queue cannot be empty to successfully perform it.)
# Follow the hints:

# use a list as your storage (just like we did with the stack)
# put() should append elements to the beginning of the list, while get()
# should remove the elements from the end of the list;
# define a new exception named QueueError (choose an exception to derive it from)
# and raise it when get() tries to operate on an empty list.

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")


class QueueError(IndexError):
    pass

# or


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
