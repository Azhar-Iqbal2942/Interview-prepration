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

    def __iter__(self):
        node = self.__head
        while node is not None:
            yield node
            node = node.next_node

    def add_last(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            self.__tail.next_node = new_node
            self.__tail = new_node

        self.__count += 1

    def add_first(self, item):
        new_node = Node(item)

        if self.is_empty():
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

    def remove(self, value):
        previous = self.__head
        current = self.__head
        target = None

        if self.__head.value == value:
            self.remove_first()
            return value

        if self.__tail.value == value:
            self.remove_last()
            return value

        while current is not None:
            if current.value == value:
                previous.next_node = current.next_node
                target = current
                current.next_node = None
                return target.value

            previous = current
            current = current.next_node
        return "Item not Found"

    def remove_first(self):
        if self.is_empty():
            raise ValueError("Empty List Error")
        if self.__head == self.__tail:
            final = self.__tail.value
            self.__head = self.__tail = None
            self.__count = 0
            return final

        second = self.__head.next_node
        first = self.__head
        self.__head.next_node = None
        self.__head = second

        self.__count -= 1

        return first.value

    def remove_last(self):
        if self.is_empty():
            raise ValueError("Empty List Error")

        if self.__head == self.__tail:
            final = self.__head.value
            self.__head = self.__tail = None
            self.__count = 0
            return final

        previous = self.__get_previous()
        last = self.__tail
        self.__tail = previous
        self.__tail.next_node = None

        self.__count -= 1
        return last.value

    def get_last(self):
        if self.is_empty():
            return None
        return self.__tail.value

    def get_first(self):
        if self.is_empty():
            return None
        return self.__head.value

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def to_array(self):
        array_converted = []
        current = self.__head
        while current != None:
            array_converted.append(current.value)
            current = current.next_node
        return array_converted

    def reverse(self):
        if self.is_empty():
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
        if self.is_empty() or k < 0:
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

    def is_empty(self):
        return self.__head == None

    def __get_previous(self):
        current = self.__head

        while current != None:
            if current.next_node == self.__tail:
                return current
            current = current.next_node
        return None


# Driver Code
def driver_code():
    lst = LinkedList()
    lst.add_last(10)
    lst.add_last(20)
    lst.add_last(30)
    lst.add_last(40)
    lst.add_last(50)
    lst.add_last(60)
    print("Removed Value : ", lst.remove(60))

    for item in lst:
        print(item.value)
