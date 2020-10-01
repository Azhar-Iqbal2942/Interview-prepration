class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end_of_word = False

    def __repr__(self):
        return str(self.char)

    def has_child(self, ch):
        return True if self.children.get(ch) is not None else False

    def add_child(self, ch):
        self.children[ch] = Node(ch)

    def get_child(self, ch):
        return self.children.get(ch)

    def get_childrens(self):
        return self.children.values()

    def has_children(self):
        return len(self.children) > 0

    def remove_child(self, ch):
        self.children.pop(ch)


class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word):
        current = self.root
        for letter in word:
            if not current.has_child(letter):
                current.add_child(letter)
            current = current.get_child(letter)
        current.is_end_of_word = True

    def contains(self, key):
        if key is None:
            return

        current = self.root
        for letter in key:
            if not current.has_child(letter):
                return False
            current = current.get_child(letter)
        return current.is_end_of_word

    def traverse(self):
        self.__traverse(self.root)

    # pre-order traversal
    def __traverse(self, root):
        print(root.char)

        for item in root.get_childrens():
            self.__traverse(item)

    def remove(self, word):
        if word is None:
            return

        self.__remove(self.root, word, 0)

    def __remove(self, root, word, index):
        if index == len(word):
            root.is_end_of_word = False
            return

        char = word[index]
        child = root.get_child(char)

        if child == None:
            return

        self.__remove(child, word, index + 1)

        if not child.has_children() and not child.is_end_of_word:
            root.remove_child(char)

    def find_words(self, prefix):
        if prefix is None:
            return
        array = []
        last_node = self.__find_last_node_of(prefix)
        self.__find_words(last_node, prefix, array)
        return array

    def __find_words(self, node, prefix, array):
        if node is None:
            return

        if node.is_end_of_word:
            array.append(prefix)
        for child in node.get_childrens():
            self.__find_words(child, prefix + child.char, array)

    def __find_last_node_of(self, prefix):
        current = self.root
        for letter in prefix:
            child = current.get_child(letter)  # return node object
            if child is None:
                return None
            current = child
        return current


if __name__ == "__main__":
    trie = Trie()
    trie.insert('car')
    trie.insert('card')
    trie.insert('care')
    trie.insert('careful')

    print(trie)
