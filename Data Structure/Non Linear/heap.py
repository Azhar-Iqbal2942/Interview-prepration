class Heap:
    def __init__(self):
        self.__array = []
        self.size = 0

    def __str__(self):
        return str(self.__array)

    def insert(self, item):
        self.__array.append(item)
        self.size += 1

        self.__bubble_up()

    def remove(self):
        if self.is_empty():
            raise IndexError("Invalid Index Error")

        item = self.__array[0]
        self.__array[0] = self.__array[self.size - 1]
        self.__array.pop()
        self.size -= 1

        self.__bubble_down()
        return item

    def max(self):
        return self.__array[0]

    def __bubble_down(self):
        # parent < children swap them
        index = 0
        while index < self.size and not self.__is_valid_parent(index):
            larger_child_index = self.__larger_child_index(index)
            self.__swap(larger_child_index, index)
            index = larger_child_index

    def is_empty(self):
        return self.size == 0

    def __larger_child_index(self, index):
        if not self.__has_left_child(index):
            return index

        if not self.__has_right_child(index):
            return self.__left_child_index(index)

        return self.__left_child_index(index) if self.__left_child(
            index) > self.__right_child(index) else self.__right_child_index(index)

    def __is_valid_parent(self, index):
        if not self.__has_left_child(index):
            return True

        if not self.__has_right_child(index):
            return self.__array[index] > self.__left_child(index)

        return self.__array[index] > self.__left_child(index) and self.__array[index] > self.__right_child(index)

    def __left_child(self, index):
        return self.__array[self.__left_child_index(index)]

    def __right_child(self, index):
        return self.__array[self.__right_child_index(index)]

    def __left_child_index(self, index):
        return (index * 2) + 1

    def __right_child_index(self, index):
        return (index * 2) + 2

    def __has_left_child(self, index):
        return self.__left_child_index(index) < self.size

    def __has_right_child(self, index):
        return self.__right_child_index(index) < self.size

    def __parent(self, index):
        return (index - 1)//2

    def __bubble_up(self):
        index = self.size - 1
        while index > 0 and self.__array[index] > self.__array[self.__parent(index)]:
            self.__swap(index, self.__parent(index))
            index = self.__parent(index)

    def __swap(self, child, parent):
        temp = self.__array[parent]
        self.__array[parent] = self.__array[child]
        self.__array[child] = temp


class PriorityQueueWithHeap:
    def __init__(self):
        self.heap = Heap()

    def __str__(self):
        return str(self.heap)

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        return self.heap.remove()

    def is_empty(self):
        return self.heap.is_empty()


if __name__ == "__main__":
    pq = PriorityQueueWithHeap()
    pq.enqueue(10)
    pq.enqueue(20)
    pq.enqueue(30)

    print(pq)
