import sys


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

    def is_bst(self):
        MIN_VALUE = ~sys.maxsize
        MAX_VALUE = sys.maxsize

        return self.__is_bst(self.root, MIN_VALUE, MAX_VALUE)

    def swap_root(self):
        temp = self.root.left_child
        self.root.left_child = self.root.right_child
        self.root.right_child = temp

    def equals(self, tree):
        if tree is None:
            return False

        return self.__equals(self.root, tree.root)

    def get_value_at_distance(self, distance):
        nodes = []
        self.__get_value_at_distance(self.root, distance, nodes)
        return nodes

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

    def __equals(self, first, second):
        if first is None and second is None:
            return True

        # pre-order Traversal
        if first is not None and second is not None:
            return first.data == second.data and self.__equals(first=first.left_child, second=second.left_child) and self.__equals(first=first.right_child, second=second.right_child)

        return False

    def __is_bst(self, root, mini, maxi):
        # base case
        if root is None:
            return True

        if root.data > maxi or root.data < mini:
            return False

        # recursive case
        return self.__is_bst(root.left_child, mini, root.data - 1) and self.__is_bst(root.right_child, root.data + 1, maxi)

    def __get_value_at_distance(self, root, distance, nodes):
        if root == None:
            return

        # base case
        if distance == 0:
            nodes.append(root.data)
            return

        # recursive case
        self.__get_value_at_distance(root.left_child, distance - 1, nodes)
        self.__get_value_at_distance(root.right_child, distance - 1, nodes)


def driver_code():
    tree1 = BinaryTree()
    tree1.insert(10)
    tree1.insert(7)
    tree1.insert(12)
    tree1.insert(11)
    tree1.insert(5)
    tree1.insert(15)
    tree1.insert(18)
   # tree1.swap_root()  # for checking purpose only

    tree2 = BinaryTree()
    tree2.insert(10)
    tree2.insert(7)
    tree2.insert(12)
    tree2.insert(11)
    tree2.insert(5)
    tree2.insert(15)
    tree2.insert(18)

    print(tree1.get_value_at_distance(2))


driver_code()
