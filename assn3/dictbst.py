#!/usr/bin/python3


from bst import *


class Dictionary:

    def __init__(self):
        """
        defines a dictionary with no parameters
        has an attribute data that points to a BST
        """
        self.data = BinarySearchTree()

    def makenull(self):
        """
        makes the dictionary empty
        """
        self.data.root = None

    def insert(self, x):
        """
        inserts x into the dictionary
        :type x: int
        """
        bst_insert(x, self.data.root)

    def delete(self, x):
        """
        deletes x from the dictionary
        :type x: int
        """
        bst_delete(x, self.data.root)

    def member(self, x):
        """
        determines if x is a member of the dictionary
        :type x: int
        """
        return bst_member(x, self.data.root)


if __name__ == '__main__':
    d = Dictionary()

