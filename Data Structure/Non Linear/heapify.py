from heap import Heap


class MaxHeap:
    def heapify(self, array):
        last_parent_index = (len(array)//2) - 1
        for index in reversed(range(last_parent_index + 1)):
            self.__heapify(array, index)

    def __heapify(self, array, index):
        larger_index = index

        left_index = (index * 2) + 1
        if left_index < len(array) and array[left_index] > array[larger_index]:
            larger_index = left_index

        right_index = (index * 2) + 2
        if right_index < len(array) and array[right_index] > array[larger_index]:
            larger_index = right_index

        if index == larger_index:
            return

        self.__swap(array, index, larger_index)
        self.__heapify(array, larger_index)

    def __swap(self, array, first, second):
        temp = array[first]
        array[first] = array[second]
        array[second] = temp

    def get_kth_largest(self, array, k):
        if k < 1 or k > len(array):
            raise IndexError
        heap = Heap()

        for number in array:
            heap.insert(number)

        for index in range(k-1):
            heap.remove()

        return heap.max()


if __name__ == "__main__":
    numbers = [5, 3, 8, 4, 1, 2]
    heap = MaxHeap()
    print(heap.get_kth_largest(numbers, 3))
