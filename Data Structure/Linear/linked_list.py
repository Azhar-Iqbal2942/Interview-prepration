"""
-> Features to Build

add_last()
add_first()
remove_first()
remove_lasy()
contains()
index_of()
size()

-> Tasks
Reverse LinkList in place.
Getting Kth node from end in one pass. 

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.__head = head
        self.__tail = tail
        self.__count = 0

    def add_last(self, item):
        new_node = Node(item)

        if self.__is_empty():
            self.__head = self.__tail = new_node
        else:
            self.__tail.next_node = new_node
            self.__tail = new_node

        self.__count += 1

    def add_first(self, item):
        new_node = Node(item)

        if self.__is_empty():
            self.__head = self.__tail = new_node
        else:
            new_node.next_node = self.__head
            self.__head = new_node

        self.__count += 1

    def index_of(self, item):
        current = self.__head
        index = 0

        while current != None:
            if current.value == item:
                return index
            current = current.next_node
            index += 1
        return -1

    def contain(self, item):
        return self.indexOf(item) != -1

    def remove_first(self):
        if self.__is_empty():
            raise ValueError("Empty List Error")
        if self.__head == self.__tail:
            self.__head = self.__tail = None
            self.__count = 0
            return

        second = self.__head.next_node
        self.__head.next_node = None
        self.__head = second

        self.__count -= 1

    def remove_last(self):
        if self.__is_empty():
            raise ValueError("Empty List Error")

        if self.__head == self.__tail:
            self.__head = self.__tail = None
            self.__count = 0
            return

        previous = self.__get_previous()
        self.__tail = previous
        self.__tail.next_node = None

        self.__count -= 1

    def to_array(self):
        array_converted = []
        current = self.__head
        while current != None:
            array_converted.append(current.value)
            current = current.next_node
        return array_converted

    def reverse(self):
        if self.__is_empty():
            return

        prev = self.__head
        current = prev.next_node

        while current != None:
            next_val = current.next_node
            current.next_node = prev

            # Update pointer positions
            prev = current
            current = next_val
        self.__tail = self.__head
        self.__head.next_node = None
        self.__head = prev

    def get_Kth_from_end(self, k):
        if self.__is_empty() or k < 0:
            return
        target = self.__head
        current = self.__head

        for x in range(k-1):
            current = current.next_node
            if current.next == None:  # In case we have no size method
                raise IndexError("Index Out of range Error")

        while current != self.__tail:
            target = target.next_node
            current = current.next_node

        return target.value

    def get_middle(self):
        target = self.__head
        current = self.__head
        while current != self.__tail and current.next_node != self.__tail:
            current = current.next_node.next_node
            target = target.next_node

        if current == self.__tail:  # for odd value
            return target.value
        else:  # for even value
            return target.value, target.next_node.value

    def has_loop(self):
        slow = self.__head
        fast = self.__head

        while fast != None and fast.next_node != None:
            fast = fast.next_node.next_node
            slow = slow.next_node

            if fast == slow:
                return True
        return False

    def size(self):
        return self.__count

    def __is_empty(self):
        return self.__head == None

    def __get_previous(self):
        current = self.__head

        while current != None:
            if current.next_node == self.__tail:
                return current
            current = current.next_node
        return None


# Driver Code
lst = LinkedList()


lst.add_last(10)
lst.add_last(20)
lst.add_last(30)
lst.add_last(40)
lst.add_last(50)
lst.add_last(60)
print(lst.has_loop())
