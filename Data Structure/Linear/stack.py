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


class ArrayStack:
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


class LinkedListStack:
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
        self.stack = LinkedListStack()
        self.expression = expression
        self.left_brackets = ['(', '[', '{', '<']
        self.right_brackets = [')', ']', '}', '>']

    def is_balanced(self):
        for char in self.expression:
            if self.left_brackets.__contains__(char):
                self.stack.push(char)

            if self.right_brackets.__contains__(char):
                if self.stack.is_empty():
                    return False

                left = self.stack.pop()
                if not self.bracket_matcher(left, char):
                    return False

        return self.stack.is_empty()

    # if match return True
    def bracket_matcher(self, left, right):
        return self.left_brackets.index(left) == self.right_brackets.index(right)


class Reverser:
    def __init__(self, item):
        self.stack = LinkedListStack()
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
    # str_reverse = Reverser('abcd')
    # print(str_reverse.string_reverser())

    exp = Expression('{[(1+2)]')
    print(exp.is_balanced())
