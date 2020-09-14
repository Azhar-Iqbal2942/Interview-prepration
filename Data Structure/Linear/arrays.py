"""
-> task
1 = add a method to find largest number
2 = add a method to find common items (pass another array to compare)
3 = add a method to reverse an array
4 = add a method to add item at given index (index,item)

-> Declaring static array
[None]*10 this will create an array of size 10


"""


class Array:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def insert(self, item):
        self.array.append(item)

    def removeAt(self, index):
        if index >= 0 and index < self.array.__len__():
            del self.array[index]
            return f"Successfully removed {index}"
        raise ValueError("Invalid Index Error")

    def indexOf(self, value):
        index = 0
        for number in self.array:
            if number == value:
                return index
            index += 1
        return -1

    def max_value(self):
        max = 0
        for number in self.array:
            if number > max:
                max = number
        return max

    def intersect(self, other_list):
        common = []
        for number in self.array:
            if other_list.indexOf(number) >= 0:
                common.append(number)
        return common

    def reverse(self):
        if self.array.__len__() > 0:
            reverse = []
            for index in reversed(range(self.array.__len__())):
                reverse.append(self.array[index])
            return reverse
        raise IndexError("Zero Index Error")

    def insertAt(self,  index, item):
        self.array.insert(index, item)


def driver_code():
    arr = Array()
    arr.insert(10)
    arr.insert(20)
    arr.insert(30)
    arr.insert(40)
    arr.insertAt(2, 60)
    print(arr)

    other_list = Array()
    other_list.insert(20)
    other_list.insert(40)
    other_list.insert(60)
    other_list.insert(80)
