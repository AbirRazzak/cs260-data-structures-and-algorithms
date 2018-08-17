#!/usr/bin/python3

class Node:
    self.children = []
    self.value = None
    self.parent = None

    def __init__(self, v = None, p = None):
        self.value = v
        self.parent = p

    def add(self, n):
        self.children.append(n)

class Tree:
    self.root = None

    def __init__(self, n = None):
        self.root = n

    def set_root(self, n):
        """
        This function is mainly used for if the user created an empty tree / makenull and wants to add a root later on
        :param n: Node to make the root
        """
        self.root = n

    def root(self):
        return self.root

    def make_null(self):
        self.root = None

    def leftmost_child(self, n):
        return n.children[0]

    def right_sibling(self, n):
        p = n.parent
        i = p.children.index(n)
        return p.children[i+1]  # Returns the child node that is index 1 after current node

    def parent(self, n):
        return n.parent

    def label(self, n):
        return n.value

def create_i(n, t):
    """
    Returns a new tree with root of value n, and children of the roots of t.
    :param n: Value of new root
    :param t: List of trees
    :return: A new tree
    """
    r = Node(n)
    new = Tree(r)
    for tree in t:
        s = tree.root()
        r.add(s)

    return new
