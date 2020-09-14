from linked_list import LinkedList
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
    def __init__(self):
        self.lst = LinkedList()

    def push(self, value):
        self.lst.add_last(value)

    def pop(self):
        return self.lst.remove_last().value

    def peek(self):
        return self.lst.get_last()

    def is_empty(self):
        return self.lst.is_empty()


def driver_code():
    ll = stackUsingLinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    ll.push(40)
    print(ll.is_empty())
