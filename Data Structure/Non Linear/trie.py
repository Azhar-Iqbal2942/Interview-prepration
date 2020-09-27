class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end_of_word = False

    def has_child(self, ch):
        return True if self.children.get(ch) is not None else False

    def add_child(self, ch):
        self.children[ch] = Node(ch)

    def get_child(self, ch):
        return self.children.get(ch)


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


if __name__ == "__main__":
    trie = Trie()
    trie.insert('cat')
    trie.insert('canada')
    print(trie.contains(None))
