#!/usr/bin/env/python3


class StackNode:
    value = None
    next = None

    def __init__(self, val=None, nxt=None):
        self.value = val
        self.next = nxt


class PointerStack:
    head = None

    def __init__(self):
        self.head = StackNode()  # Empty node is the head when creating stack

    def TOP(self):
        if self.head.value is None:
            return -1
        else:
            return self.head.value

    def POP(self):
        # Implementing it like it does in the book, pop does not return anything.
        if self.head.value is not None:
            second_node = self.head.next
            self.head = second_node
        else:
            return -1

    def PUSH(self, x):
        if self.head.value is None:
            # If the stack is empty then the head value is None
            # Just change the value of the head to x
            self.head.value = x
        else:
            # Move over the currentHead and insert a new node at the head "top of stack"
            new_top = StackNode(x, self.head)
            self.head = new_top

    def EMPTY(self):
        return self.head.value is None

    def MAKENULL(self):
        empty_node = StackNode()
        self.head = empty_node

    def display(self):
        current = self.head
        while current is not None:
            print("{0} ".format(current.value))
            current = current.next
