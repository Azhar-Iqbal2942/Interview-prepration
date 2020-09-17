from stack import ArrayStack
from linked_list import LinkedList


class ArrayQueue:
    def __init__(self):
        self.array = [0]*5
        self.count = 0
        self.front = -1
        self.rear = 0

    def __str__(self):
        return str(self.array)

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is already full")

        self.array[self.rear] = item
        self.rear = (self.rear + 1) % len(self.array)
        self.count += 1
        if self.front == -1:
            self.front = 0

    def dequeue(self):
        if self.is_empty():
            self.front = -1
            self.rear = 0
            raise IndexError("Empty List Error")

        value = self.array[self.front]
        self.array[self.front] = 0
        self.front = (self.front + 1) % len(self.array)
        self.count -= 1
        return value

    def peek(self):
        return self.array[self.front]

    def is_empty(self):
        return len(self.array) == 0

    def is_full(self):
        return self.count == len(self.array)

    def size(self):
        return self.count


class StackQueue:
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()
        self.count = 0

    def enqueue(self, item):
        self.stack1.push(item)
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Empty Queue Error")

        self.moveStack1ToStack2()
        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("Empty Queue Error")

        self.moveStack1ToStack2()
        return self.stack2.peek()

    def moveStack1ToStack2(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()


"""
A smimple priority Queue using Array .
Remember this is linear Array not Circular Array 

"""


class PriorityQueue:
    def __init__(self):
        self.array = [0] * 5
        self.count = 0
        self.front = 0

    def __str__(self):
        return ', '.join(map(str, self.array))

    def enqueue(self, item):
        if self.is_full():
            raise ValueError("Queue is already full")

        if self.count == 0:
            self.array[self.count] = item
            self.count += 1
        else:
            counter = self.shift_items_to_right(item)
            self.array[counter] = item
            self.count += 1

    def shift_items_to_right(self, value):
        counter = self.count - 1

        for num in range(self.count):
            if self.array[counter] > value:
                self.array[counter + 1] = self.array[counter]
                counter -= 1
            else:
                break

        return counter + 1

    def dequeue(self):
        if self.is_empty():
            return

        self.array[self.front] = 0
        self.front += 1

    def peek(self):
        return self.array[0]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.array)


def driver_code():
    pq = PriorityQueue()
    pq.enqueue(10)
    pq.enqueue(7)
    pq.enqueue(12)
    pq.enqueue(18)
    pq.enqueue(4)
    pq.dequeue()
    pq.dequeue()

    print(pq)
