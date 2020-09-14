from linked_list import LinkedList
"""
Basic Operations 
push()
pop()
peek()
size()
isEmpty()

-> Tasks
Build stack using array
Build stack using Linked List

Build a string reverser
Build an Expression Checker

"""


class stackUsingArray:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        return self.array.pop()

    def peek(self):
        return self.array[-1]

    def is_empty(self):
        return self.array.__len__() == 0


class stackUsingLinkedList:
    def __init__(self):
        self.lst = LinkedList()

    def push(self, value):
        self.lst.add_last(value)

    def pop(self):
        return self.lst.remove_last()

    def peek(self):
        return self.lst.get_last()

    def is_empty(self):
        return self.lst.is_empty()


class Expression:
    def __init__(self, expression):
        self.stack = stackUsingLinkedList()
        self.expression = expression

    def is_balanced(self):
        for char in self.expression:
            if self.is_left_bracket(char):
                self.stack.push(char)

            if self.is_right_bracket(char):
                if self.stack.is_empty():
                    return False

                left = self.stack.pop()
                if self.bracket_matcher(left, char):
                    return False

        return self.stack.is_empty()

    def is_left_bracket(self, char):
        return char == "(" or char == "[" or char == "{" or char == "<"

    def is_right_bracket(self, char):
        return char == ")" or char == "]" or char == "}" or char == ">"

    # if error return True else False
    def bracket_matcher(self, left, right):
        return ((right == ")" and left != "(") or (right == "]" and left != "[") or (right == "}" and left != "{") or (right == ">" and left != "<"))


class Reverser:
    def __init__(self, item):
        self.stack = stackUsingLinkedList()
        self.item = item

    def string_reverser(self):
        reverse = ''
        for char in self.item:
            self.stack.push(char)

        while not self.stack.is_empty():
            r = self.stack.pop()
            reverse = reverse + str(r)

        return reverse


def driver_code():
    str_reverse = Reverser('abcd')
    print(str_reverse.string_reverser())
