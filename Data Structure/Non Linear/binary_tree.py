class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Node = {self.data}"


class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, item):
        node = Node(item)
        current = self.root

        # if tree is empty
        if self.root == None:
            self.root = node
            self.count += 1
            return

        while True:
            if item > current.data:
                if current.right_child == None:
                    current.right_child = node
                    self.count += 1
                    break
                current = current.right_child
            else:
                if current.left_child == None:
                    current.left_child = node
                    self.count += 1
                    break
                current = current.left_child

    def find(self, item):
        current = self.root

        if item == current.data:
            return True

        while current is not None:
            if item > current.data:
                current = current.right_child
            elif item < current.data:
                current = current.left_child
            else:
                return True
        return "Not Found"

    def traverse(self):
        self.__traverse_post_order(self.root)

    def height(self):
        return self.__height(self.root)

    def min(self):
        if self.root == None:
            return

        current = self.root
        last = current

        while current is not None:
            last = current
            current = current.left_child

        return last.data

    def max(self):
        if self.root == None:
            return

        current = self.root
        last = current

        while current is not None:
            last = current
            current = current.right_child

        return last.data

    def __traverse_pre_order(self, root):
        if root == None:
            return

        print(root.data)
        self.__traverse_pre_order(root.left_child)
        self.__traverse_pre_order(root.right_child)

    def __traverse_in_order(self, root):
        if root == None:
            return

        self.__traverse_in_order(root.left_child)
        print(root.data)
        self.__traverse_in_order(root.right_child)

    def __traverse_post_order(self, root):
        if root == None:
            return

        self.__traverse_post_order(root.left_child)
        self.__traverse_post_order(root.right_child)
        print(root.data)

    def __height(self, root):
        if root is None:
            return -1

        if self.__is_leaf(root):
            return 0

        return 1 + max(self.__height(root.left_child), self.__height(root.right_child))

    def __is_leaf(self, root):
        return root.left_child == None and root.right_child == None


def driver_code():
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(7)
    tree.insert(12)
    tree.insert(11)
    tree.insert(5)
    tree.insert(15)
    tree.insert(18)
    print(tree.max())


driver_code()
