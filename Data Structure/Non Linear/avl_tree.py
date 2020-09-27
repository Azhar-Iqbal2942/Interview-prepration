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

    def __str__(self):
        return self.root

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

        self.__set_height(root)
        return self.__auto_balancer(root)

    def __auto_balancer(self, root):
        if self.__is_left_heavy(root):
            if self.__balance_factor(root.left_child) < 0:
                root.left_child = self.__rotate_left(root.left_child)
            return self.__rotate_right(root)

        if self.__is_right_heavy(root):
            if self.__balance_factor(root.right_child) > 0:
                root.right_child = self.__rotate_right(root.right_child)
            return self.__rotate_left(root)

        return root

    def __rotate_left(self, root):
        new_root = root.right_child

        root.right_child = new_root.left_child
        new_root.left_child = root

        # now update heights
        self.__set_height(root)
        self.__set_height(new_root)

        return new_root

    def __rotate_right(self, root):
        new_root = root.left_child

        root.left_child = new_root.right_child
        new_root.right_child = root

        # update heights
        self.__set_height(root)
        self.__set_height(new_root)

        return new_root

    def __set_height(self, node):
        node.height = max(self.__height(node.left_child),
                          self.__height(node.right_child)) + 1

    def __is_left_heavy(self, node):
        return self.__balance_factor(node) > 1

    def __is_right_heavy(self, node):
        return self.__balance_factor(node) < -1

    def __balance_factor(self, node):
        return 0 if node is None else self.__height(node.left_child) - self.__height(node.right_child)

    def __height(self, root):
        return -1 if root == None else root.height


tree = AVLTree()
tree.insert(20)
tree.insert(10)
tree.insert(30)
tree.insert(15)
tree.insert(13)


print(tree.root.left_child)


# print(tree.height())
