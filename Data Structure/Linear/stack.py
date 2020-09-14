"""
Basic Operations 
push()
pop()
peek()
size()
isEmpty()

-> Tasks
Build stack using array
Build stack using Linked List

"""


class stackUsingArray:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        return self.array.pop()

    def peek(self):
        return self.array[-1]

    def is_empty(self):
        return self.array.__len__() == 0


class stackUsingLinkedList:
    pass


def driver_code():
    arr = stackUsingArray()
    arr.push(10)
    arr.push(20)
    arr.push(30)
    arr.push(40)
    print(arr.pop())
    print(arr.is_empty())


driver_code()
