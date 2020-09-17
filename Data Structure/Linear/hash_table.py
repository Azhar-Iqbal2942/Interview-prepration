from linked_list import LinkedList


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.array = [None] * 5

    def __str__(self):
        return str(self.array)

    def put(self, key, value):
        index = self.hash_func(key)

        if self.array[index] == None:
            self.array[index] = LinkedList()
            self.array[index].add_last(Entry(key, value))
            return

        # Check if key already exist
        ll = self.array[index]
        bucket = ll.get_head()
        while bucket != None:
            if bucket.value.key == key:
                bucket.value.value = value
                return
            bucket = bucket.next_node

        ll.add_last(Entry(key, value))

    def get(self, key):

        index = self.hash_func(key)

        if self.array[index] == None:
            raise ValueError("Value Not Exist")

        ll = self.array[index]
        bucket = ll.get_head()

        while bucket != None:
            if bucket.value.key == key:
                return bucket.value.value
            bucket = bucket.next_node
        return "Not Found"

    def remove(self, key):
        index = self.hash_func(key)
        ll = self.array[index]

        for item in ll:
            if item.value.key == key:
                return ll.remove(item.value).value

    def hash_func(self, key):
        """
        Un-Comment this code if key is String
        """
        # hash_code = 0
        # for ch in key:
        #     hash_code = hash_code + ord(ch)

        return key % len(self.array)


def driver_code():
    table = HashTable()
    table.put(6, 'A')
    table.put(8, 'B')
    table.put(11, 'C')

    print(table.remove(6))
    print(table.get(6))
