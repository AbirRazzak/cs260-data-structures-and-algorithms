#!/usr/bin/python3


class BSTNode:

    def __init__(self, v=None):
        """
        defines a BST Node with an optional parameter for its value
        sets 2 attributes, left_child and right_child as None
        :type v: int
        """
        self.element = v
        self.left_child = None
        self.right_child = None

    def append(self, x):
        """
        replaces the BSTNode with a new BSTNode
        :type x: BSTNode
        """
        self = x


class BinarySearchTree:

    def __init__(self, r=None):
        """
        defines a BST with an optional parameter to specify the root
        :type r: BSTNode
        """
        self.root = r


def bst_member(x, a):
    """
    returns if x is a member of the BST
    :type x: int
    :type a: BSTNode
    """
    if a is None:
        return False

    if a.element == x:
        return True

    if x < a.element:
        return bst_member(x, a.left_child)

    if x > a.element:
        return bst_member(x, a.right_child)


def bst_insert(x, a):
    """
    inserts an int into the BST
    :type x: int
    :type a: BSTNode
    """
    if a is None:
        a.append(BSTNode(x))

    elif x < a.element:
        bst_insert(x, a.left_child)

    elif x > a.element:
        bst_insert(x, a.right_child)

    # if x = A.element, we do nothing
    # x is already in the set


def delete_min(a):
    """
    returns and removes the smallest element from set A
    :type a: BSTNode
    """
    if a.left_child is None:
        # A points to the smallest element
        m = a.element
        a.append(a.right_child)
        return m
    else:
        # the node pointed to by A has a left child
        return delete_min(a.left_child)


def bst_delete(x, a):
    """
    remove x from set A
    :type x: int
    :type a: BSTNode
    """
    if a.element is not None:
        if x < a.element:
            bst_delete(x, a.left_child)

        elif x > a.element:
            bst_delete(x, a.right_child)

        # if we reach here, x is at the node pointed to by A
        elif (a.left_child is None) and (a.right_child is None):
            a.append(None)

        elif a.left_child is None:
            a.append(a.right_child)

        elif a.right_child is None:
            a.append(a.left_child)

        else:
            # both children are present
            a.element = delete_min(a.right_child)
