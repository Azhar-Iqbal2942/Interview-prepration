class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 0

    def __str__(self):
        return f"Value = {self.value}"


class AVLTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __insert(self, root, value):
        # base case
        if root == None:
            self.count += 1
            return Node(value)

        # recursive case
        if value > root.value:
            root.right_child = self.__insert(root.right_child, value)
        else:
            root.left_child = self.__insert(root.left_child, value)

        root.height = max(self.__height(root.left_child),
                          self.__height(root.right_child)) + 1
        print(root.height)

        return root

    def __height(self, root):
        return -1 if root == None else root.height

    def __is_leaf(self, root):
        return root.left_child == None and root.right_child == None


tree = AVLTree()
tree.insert(10)
tree.insert(8)


# print(tree.height())
