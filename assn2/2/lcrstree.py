#!/usr/bin/python3

class Node:
    self.parent = None  # type: Node
    self.LeftMostChild = None  # type: Node
    self.RightSibling = None  # type: Node
    self.value = None

    def __init__(self, v: Node = None, p: Node = None) -> None:
        self.value = v
        self.parent = p

    def set_child(self, n: Node) -> None:
        self.LeftMostChild = n

    def set_sibling(self, n: Node) -> None:
        self.RightSibling = n

class Tree:
    self.root = None  # type: Node

    def __init__(self, r: Node = None) -> None:
        self.root = r

    def set_root(self, n: Node) -> None:
        """
        This function is mainly used for if the user created an empty tree / makenull and wants to add a root later on
        :param n: Node to make the root
        """
        self.root = n

    def parent(self, n: Node) -> Node:
        return n.parent

    def leftmost_child(self, n: Node) -> Node:
        return n.LeftMostChild

    def right_sibling(self, n: Node) -> Node:
        return n.RightSibling

    def label(self, n: Node):
        return n.value

    def root(self) -> Node:
        return self.root

    def make_null(self) -> None:
        self.root = None

def create_i(v, t: List) -> Tree:
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
