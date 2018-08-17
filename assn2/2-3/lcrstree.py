#!/usr/bin/python3

class Node:

    def __init__(self, v = None, p = None):
        self.value = v
        self.parent = p
        self.LeftMostChild = None  # type: Node
        self.RightSibling = None  # type: Node

    def set_child(self, n):
        self.LeftMostChild = n

    def set_sibling(self, n):
        self.RightSibling = n

class Tree:

    def __init__(self, r = None):
        self.root = r  # type: Node

    def set_root(self, n):
        """
        This function is mainly used for if the user created an empty tree / makenull and wants to add a root later on
        :param n: Node to make the root
        """
        self.root = n

    def parent(self, n):
        return n.parent

    def leftmost_child(self, n):
        return n.LeftMostChild

    def right_sibling(self, n):
        return n.RightSibling

    def label(self, n):
        return n.value

    def root(self):
        return self.root

    def make_null(self):
        self.root = None

def create_i(v, t):
    r = Node(v)
    new = Tree(r)

    r.LeftMostChild = t.pop(0).root()  # Sets the leftmost child of the root to the root of the first tree in t
    i = new.leftmost_child(r)
    i.parent = r

    for tree in t:
        s = tree.root()
        i.RightSibling = s
        i = i.RightSibling
        i.parent = r

    return new
